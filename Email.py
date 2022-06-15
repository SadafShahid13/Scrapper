from __future__ import print_function

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

SCOPES = ['https://mail.google.com/','https://www.googleapis.com/auth/gmail.modify','https://www.googleapis.com/auth/gmail.compose','https://www.googleapis.com/auth/gmail.send']


class Email():
    def gmailSendMail(self,msg,to,subject):
    
        load_dotenv()
        logger = Logger()

        creds = None

        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                try:
                    flow = InstalledAppFlow.from_client_secrets_file(
                    os.getenv('SECRET_JSON_PATH'), SCOPES)
                except:
                    logger.criticalLog("Gmail Credentials Missing")
                    exit()
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

            send_email = (service.users().messages().send
                            (userId="me", body=create_message).execute())
            logger.infoLog("Email with ID: " + send_email['id'] + " Sent")
        except HttpError:
            logger.errorLog("HttpError: ")
            send_email = None
        return send_email
    
    def gmailSendEmailAttachment(self,msg,to,subject,attachment):
    
        load_dotenv()
        logger = Logger()

        creds = None

        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                try:
                    flow = InstalledAppFlow.from_client_secrets_file(
                    os.getenv('SECRET_JSON_PATH'), SCOPES)
                except:
                    logger.criticalLog("Gmail Credentials Missing")
                    exit()
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

            with open(attachment, 'rb') as fp:
                message.add_attachment(fp.read(),
                                maintype='application',
                                subtype='xlsx',
                                filename='iPhones.xlsx')

            encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
                .decode()

            create_message = {
                'raw': encoded_message
            }

            send_email = (service.users().messages().send
                            (userId="me", body=create_message).execute())
            logger.infoLog("Email with ID: " + send_email['id'] + " Sent with an attachment")
        except HttpError:
            logger.errorLog("HttpError: ")
            send_email = None
        return send_email

if __name__ == "__main__":

    mailer = Email()
    
    mailer.gmailSendEmailAttachment("The Requested Excel file is attached","sadafshahid@iut-dhaka.edu","iPhone Data","Outputs/iPhones.xlsx")

    # mailer.gmailSendMail("What's Up","sadafshahid@iut-dhaka.edu","First Try")