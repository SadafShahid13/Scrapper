import os
from twilio.rest import Client
from dotenv import load_dotenv
from Logger import Logger

class SMS:
    def sendSMS(self, msg):

        load_dotenv()
        logger = Logger()

        toNumber = os.getenv('MY_MOBILE_NUMBER')
        fromNumber = os.getenv('TWILIO_NUMBER')
        account_sid = os.getenv('ACCOUNT_SID')
        auth_token  = os.getenv('AUTH_TOKEN')
    
        client = Client(account_sid, auth_token)
        logger.infoLog("Sending SMS to " + toNumber)
    
        try:
            message = client.messages \
                .create(
                    body=msg,
                    from_=fromNumber,
                    to=toNumber
                )
            print(message.sid)
            logger.infoLog("SMS Sent")
        except Exception:
            logger.errorLog("Exception")

if __name__ == "__main__":

    sms = SMS()

    # sms.sendSMS("GG")