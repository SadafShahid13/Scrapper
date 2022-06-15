from Logger import Logger
from openpyxl import Workbook
import openpyxl

class ExcelController:
    logger = Logger()
    def createXlsxFile(self, path):
        book = Workbook()
        book.save(path)

    def inputData(self, path, data):
        book = openpyxl.load_workbook(path)
        sheet = book.active
        for row in data:
            sheet.append(row)
        book.save(path)

if __name__ == "__main__":
    
    excelControl = ExcelController()
    excelControl.createXlsxFile("Outputs/iPhones.xlsx")