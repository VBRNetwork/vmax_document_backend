from documentmanager.celery import app
import os
import msal
import requests
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from io import BytesIO
from .models import Documents
import uuid


class EmailReceiver:

    def __init__(self):
        self.client_id = 'e167e27b-91d5-4909-a409-9daa838affd3'
        self.client_secret = 'cQJ8Q~SN7mUv1sgLEOURuBuW-tbCzrhznvnRuayY'
        self.tenant_id = '1999d1ab-f68f-4f7a-b94e-9aa8a84542af'
        self.scopes = ["https://graph.microsoft.com/.default"]
        self.authority_url = f"https://login.microsoftonline.com/{self.tenant_id}"
        self.latest_attachment_id = None

    def get_token(self):
        app = msal.ConfidentialClientApplication(
            client_id=self.client_id,
            client_credential=self.client_secret,
            authority=self.authority_url)

        result = app.acquire_token_for_client(scopes=self.scopes)
        if "access_token" in result:
            return result["access_token"]
        else:
            raise ValueError("Failed to obtain access token")

    def get_messages(self):
        userId = "stefan@veelancing.io"
        endpoint = f'https://graph.microsoft.com/v1.0/users/{userId}/messages'
        access_token = self.get_token()
        r = requests.get(endpoint,
                         headers={'Authorization': 'Bearer ' + access_token})
        if r.ok:
            data = r.json()
            return data['value']
        else:
            raise ValueError("Failed to retrieve emails")
    def get_attachments(self):
        userId = "stefan@veelancing.io"
        access_token = self.get_token()
        data = self.get_messages()
        mails_with_attachments = list()
        for msg in data:
            if msg.get('hasAttachments'):
                aid = msg.get("id")
                if aid != self.latest_attachment_id:
                    attachment_response = requests.get(
                        url=f'https://graph.microsoft.com/v1.0/users/{userId}/messages/{aid}/attachments',
                        headers={'Authorization': 'Bearer ' + access_token}
                    )
                    jsonified_response = attachment_response.json()
                    attachment_id = jsonified_response.get('value')[0].get('id')
                    attachment_name = jsonified_response.get('value')[0].get('name')
                    attachment_extension = jsonified_response.get('value')[0].get('name').split('.')[-1]
                    attachment_content_type = jsonified_response.get('value')[0].get('contentType')
                    attachment_sender = msg.get('from').get('emailAddress').get('address')
                    download_response = requests.get(
                        url=f'https://graph.microsoft.com/v1.0/users/{userId}/messages/{aid}/attachments/{attachment_id}/$value',
                        headers={'Authorization': 'Bearer ' + access_token},
                        stream=True)
                    file_size = len(download_response.content)
                    buffer = BytesIO(download_response.content)
                    buff_val = buffer.getvalue()
                    content = ContentFile(buff_val)
                    attachment = InMemoryUploadedFile(
                        content, None, f"{attachment_name}", f"{attachment_content_type}", len(buff_val), None
                    )
                    document_id = uuid.uuid4()
                    existing_document = Documents.objects.filter(document_attachment_id=attachment_id).exists()
                    if existing_document is False and 'Contract' or 'contract' in attachment_name:
                        Documents.objects.create(
                            document_attachment_id=attachment_id,
                            document_name=attachment_name,
                            file=attachment,
                            document_has_attachment=True,
                            document_id=document_id,
                            document_email_uploader=attachment_sender,
                            document_extension=attachment_extension,
                            document_type='Contract'
                        )
                    elif existing_document is False and 'Invoice' or 'invoice' or 'Factura' or 'factura' in attachment_name:
                        Documents.objects.create(
                            document_attachment_id=attachment_id,
                            document_name=attachment_name,
                            file=attachment,
                            document_has_attachment=True,
                            document_id=document_id,
                            document_email_uploader=attachment_sender,
                            document_extension=attachment_extension,
                            document_type='Supplier Invoice'
                        )
                    elif existing_document is False and 'NDA' or 'nda' or 'confidentialitate' or 'Confidentialitate' in attachment_name:
                        Documents.objects.create(
                            document_attachment_id=attachment_id,
                            document_name=attachment_name,
                            file=attachment,
                            document_has_attachment=True,
                            document_id=document_id,
                            document_email_uploader=attachment_sender,
                            document_extension=attachment_extension,
                            document_type='NDA'
                        )
                    elif existing_document is False:
                        Documents.objects.create(
                            document_attachment_id=attachment_id,
                            document_name=attachment_name,
                            file=attachment,
                            document_has_attachment=True,
                            document_id=document_id,
                            document_email_uploader=attachment_sender,
                            document_extension=attachment_extension,
                            document_type='Document'
                        )
                    self.latest_attachment_id = aid
                    mails_with_attachments.append(aid)
        return mails_with_attachments
@app.task
def initialize_email_receiver():
    email_receiver = EmailReceiver()
    email_receiver.get_attachments()
    print("Done")
    