from Logger import Logger
from openpyxl import Workbook
import openpyxl

class ExcelController:
    logger = Logger()
    def createXlsxFile(self, path):
        try:
            book = Workbook()
            book.save(path)
            ExcelController.logger.infoLog("Xlsx file created")
        except:
            ExcelController.logger.errorLog("Xlsx file not created")
            exit()
    def inputData(self, path, data):
        try:
            book = openpyxl.load_workbook(path)
            sheet = book.active
            for row in data:
                sheet.append(row)
            book.save(path)
            ExcelController.logger.infoLog("Data added to Xlsx file")
        except:
            ExcelController.logger.errorLog("Data Could not be added to Xlsx file")
            exit()

if __name__ == "__main__":
    
    excelControl = ExcelController()
    excelControl.createXlsxFile("Outputs/iPhones.xlsx")