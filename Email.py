from __future__ import print_function
from cmath import log

import os
from dotenv import load_dotenv

import base64
from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from Logger import Logger

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/','https://www.googleapis.com/auth/gmail.modify','https://www.googleapis.com/auth/gmail.compose','https://www.googleapis.com/auth/gmail.send']


class Email():
    def gmail_send_mail(self,msg,to,subject):

        load_dotenv()
        logger = Logger()

        creds = None

        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    os.getenv('SECRET_JSON_PATH'), SCOPES)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('gmail', 'v1', credentials=creds,cache_discovery=False)
            message = EmailMessage()

            message.set_content(msg)

            message['To'] = to
            message['From'] = os.getenv('FROM')
            message['Subject'] = subject

            encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
                .decode()

            create_message = {
                'raw': encoded_message
            }
            # pylint: disable=E1101
            send_email = (service.users().messages().send
                            (userId="me", body=create_message).execute())
            logger.infoLog("Email with ID: " + send_email['id'] + " Sent")
        except HttpError:
            logger.errorLog("HttpError: ")
            send_email = None
        return send_email

if __name__ == "__main__":

    mailer = Email()
    
    mailer.gmail_send_mail("What's Up","sadafshahid@iut-dhaka.edu","First Try")