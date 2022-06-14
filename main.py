# Python program to demonstrate
# selenium

# import webdriver
from Logger import Logger
from selenium import webdriver
from SMS import SMS
from Email import Email

def main():
    logger = Logger()
    sms = SMS()
    mailer = Email()

    # Uncomment the next line to receive SMS at App Start
    # sms.sendSMS("App Started")

    # create webdriver object
    driver = webdriver.Chrome(executable_path='C:\ChromeWebDriver\chromedriver.exe')
    logger.infoLog("Webdriver object created")

    # get google.com
    linkText = "https://google.com"
    driver.get(linkText)
    logger.infoLog('Opened Browser at ' + linkText)

    driver.close()
    logger.infoLog('Closed Browser')

    # Uncomment to send an email
    # mailer.gmail_send_mail("msg","to","subject")

    # Uncomment the next line to receive SMS at App End
    # sms.sendSMS("App Ended")

if __name__ == "__main__":
    main()