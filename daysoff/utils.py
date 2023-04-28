import msal
from django.conf import settings
import requests

def new_email_sender(send_to, subject, message):
    client_id = settings.EMAIL_CLIENT_ID
    client_secret = settings.EMAIL_CLIENT_SECRET
    tenant_id = settings.EMAIL_TENANT_ID
    authority = f"https://login.microsoftonline.com/{tenant_id}"

    app = msal.ConfidentialClientApplication(
        client_id=client_id,
        client_credential=client_secret,
        authority=authority,
    )

    scopes = settings.EMAIL_SCOPES

    result = None
    result = app.acquire_token_silent(scopes, account=None)

    if not result:
        print(
            "No suitable token exists in cache. Let's get a new one from Azure Active Directory."
        )
        result = app.acquire_token_for_client(scopes=scopes)

    if "access_token" in result:
        print("Access token is " + result["access_token"])

    if "access_token" in result:
        send_from = settings.EMAIL_SEND_FROM
        endpoint = (
            f"https://graph.microsoft.com/v1.0/users/{send_from}/sendMail"
        )
        email_msg = {
            "Message": {
                "Subject": subject,
                "Body": {"ContentType": "HTML", "Content": message},
                "ToRecipients": [{"EmailAddress": {"Address": send_to}}],
            },
            "SaveToSentItems": "true",
        }
        r = requests.post(
            endpoint,
            headers={"Authorization": "Bearer " + result["access_token"]},
            json=email_msg,
        )
        if r.ok:
            print("Sent email successfully")
        else:
            print(r.json())
    else:
        print(result.get("error"))
        print(result.get("error_description"))
        print(result.get("correlation_id"))