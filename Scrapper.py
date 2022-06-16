from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Logger import Logger

class Scrapper:
    logger = Logger()

    try:
        pathToDriver = "M:\Projects\Webdrivers\ChromeWebDriver\chromedriver.exe"
    except:
        logger.criticalLog("Driver not Found")
        exit()

    driver = webdriver.Chrome(executable_path=pathToDriver)
    logger.infoLog("Webdriver object created")

    def openBrowser(self, linkText):
        Scrapper.driver.get(linkText)
        Scrapper.logger.infoLog('Opened Browser at ' + linkText)
    
    def findElementByXpath(self, xpath):
        try:
            element = Scrapper.driver.find_element(By.XPATH, xpath)
            Scrapper.logger.infoLog("Element Found")
            return element
        except:
            Scrapper.logger.errorLog("Element Not Found. Closing Browser and App")
            Scrapper.closeBrowser()
            exit()
    
    def findElementsByCSS_Selector(self, css_selector):
        try:
            element = Scrapper.driver.find_elements(By.CSS_SELECTOR, css_selector)
            Scrapper.logger.infoLog("Elements Found")
            return element
        except:
            Scrapper.logger.errorLog("Elements Not Found. Closing Browser and App")
            Scrapper.closeBrowser()
            exit()
        

    def findElementByCSS_Selector(self, css_selector):
        try:
            element = Scrapper.driver.find_element(By.CSS_SELECTOR, css_selector)
            Scrapper.logger.infoLog("Element Found")
            return element
        except:
            Scrapper.logger.errorLog("Element Not Found. Closing Browser and App")
            Scrapper.closeBrowser()
            exit()

    def findElementByID(self,id):
        try:
            element = Scrapper.driver.find_element(By.ID, id)
            Scrapper.logger.infoLog("Element Found")
            return element
        except:
            Scrapper.logger.errorLog("Element Not Found. Closing Browser and App")
            Scrapper.closeBrowser()
            exit()

    def typeTextIntoElement(self, element, text):
        try:
            element.send_keys(text)
            Scrapper.logger.infoLog("Text entered into element")
        except:
            Scrapper.logger.errorLog("Text Could not be typed into element. Closing Browser and App")
            Scrapper.closeBrowser()
            exit()
    
    def clickElement(self, element):
        try:
            element.click()
            Scrapper.logger.infoLog("Element Clicked Upon")
        except:
            Scrapper.logger.errorLog("Could not click element. Closing Browser and App")
            Scrapper.closeBrowser()
            exit()

    def waitForElement(self,element):
        WebDriverWait(Scrapper.driver,5).until(EC.visibility_of(element))
    
    def waitForNSeconds(self,n):
        Scrapper.driver.implicitly_wait(n)
        Scrapper.logger.infoLog("Waited for "+ str(n) + " seconds")

    def closeCurrentTab(self):
        Scrapper.driver.close()
        Scrapper.logger.infoLog('Closed Tab')
    
    def closeBrowser(self):
        Scrapper.driver.quit()
        Scrapper.logger.infoLog('Closed Browser')
    




if __name__ == "__main__":
    scrapper = Scrapper()