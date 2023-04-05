import os
import msal
import requests
from time import sleep
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext


def convert_doc_to_pdf(file):
    os.system(f"abiword --to=pdf {file}")

def get_sharepoint_file(url):
    url = 'https://veelancingio.sharepoint.com'
    app_principal = {
    'client_id': '0fdec7e3-85c0-40cb-8390-9eee1edaf0d9',
    'client_secret': 'JTE1aRRdgCmDiiN5ryfnavQrx3TvO17Fl4iAT19hBKU=',
}

    credentials = ClientCredential(app_principal['client_id'], app_principal['client_secret'])
    ctx = ClientContext(url).with_credentials(credentials)
    web = ctx.web
    ctx.load(web)
    ctx.execute_query()
    print("Web site title: {0}".format(web.properties['Title']))

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
                    download_response = requests.get(
                        url=f'https://graph.microsoft.com/v1.0/users/{userId}/messages/{aid}/attachments/{attachment_id}/$value',
                        headers={'Authorization': 'Bearer ' + access_token},
                        stream=True)
                    file_size = len(download_response.content)
                    save_folder = '/home/sectumsempra/deathly-hallows/scripts/python/emails/msal/attachments'
                    with open(os.path.join(save_folder, attachment_name), 'wb') as f:
                        f.write(download_response.content)
                        print("Saved attachment to " + os.path.join(save_folder, attachment_name))
                    self.latest_attachment_id = aid
                    mails_with_attachments.append(aid)
        return mails_with_attachments
