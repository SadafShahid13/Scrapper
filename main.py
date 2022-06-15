from Logger import Logger
from SMS import SMS
from Email import Email
from Scrapper import Scrapper
from Excel_Controller import ExcelController
import os

def main():
    logger = Logger()
    sms = SMS()
    mailer = Email()
    scrapper = Scrapper()
    excelControl = ExcelController()

    # Uncomment the next line to receive SMS at App Start
    # sms.sendSMS("App Started")

    amazonText = "https://www.amazon.com"
    scrapper.openBrowser(amazonText)

    searchText = "Iphone 12"
    searchBarElement = scrapper.findElementByXpath("/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
    scrapper.typeTextIntoElement(searchBarElement, searchText)

    submitButtonElement = scrapper.findElementByCSS_Selector(".nav-search-submit-text.nav-sprite.nav-progressive-attribute")
    scrapper.clickElement(submitButtonElement)

    filterButtonElement = scrapper.findElementByXpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[2]/ul/li[2]/span/a/span")
    scrapper.clickElement(filterButtonElement)

    ListCount = 10
    iPhoneList = [["Text", "Price", "Description", "Link"]]
    textList = []
    priceList = []
    linkList = []
    descList = []
    
    while (ListCount > 0):
        scrapper.waitForNSeconds(5)
        nextButtonElement = scrapper.findElementByCSS_Selector(".s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator")
        itemElement = scrapper.findElementsByCSS_Selector(".a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
        for a in itemElement:
            if ("iPhone 12 Pro" in a.text):
                textList.append(a.text)
                linkList.append(a.get_attribute('href'))
                ListCount -= 1
            if (ListCount == 0):
                break
        scrapper.clickElement(nextButtonElement)
    
    for i in range(10):
        scrapper.openBrowser(linkList[i])
        scrapper.waitForNSeconds(5)
        priceElement = scrapper.findElementByCSS_Selector(".a-price.a-text-price.a-size-medium.apexPriceToPay")
        priceList.append(priceElement.text)
        descElement = scrapper.findElementByID("renewedProgramDescriptionAtf")
        descList.append(descElement.text)
        iPhoneList.append([textList[i],priceList[i],descList[i],linkList[i]])
    
    scrapper.closeBrowser()
    
    excelPath = "Outputs/iPhones.xlsx"
    if(os.path.exists(excelPath)):
        pass
    else:
        excelControl.createXlsxFile(excelPath)
    
    excelControl.inputData(excelPath, iPhoneList)
    
    # Uncomment to send an email with attachment
    # mailer.gmailSendEmailAttachment("What's Up","sadafshahid@iut-dhaka.edu","First Try",excelPath)

    # Uncomment to send an email
    # mailer.gmailSendMail("msg","to","subject")

    # Uncomment the next line to receive SMS at App End
    # sms.sendSMS("App Ended")

if __name__ == "__main__":
    main()