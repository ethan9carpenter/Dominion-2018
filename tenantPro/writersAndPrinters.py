from getAllIncome import getAllIncome
import gspread
from tenantPro import constants
from oauth2client.service_account import ServiceAccountCredentials

def writeToGoogleDrive(year):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('gdClientInfoDominion.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("tenantProSheet").get_worksheet(2012-year)

    incomeList = getAllIncome(year)
    
    for i in range(len(incomeList)):
        row = buildRow(incomeList[i])
        sheet.insert_row(row, i+1)
        
def buildRow(incomeList):
    address = incomeList[constants.addressKey]
    individualIncomeList = incomeList[constants.netIncomeKey]
    row = [address] + individualIncomeList
    
    return row

def printWithTabs(year):
    allIncome = getAllIncome(year)
    
    for propertyDetail in allIncome:
        address = propertyDetail[constants.addressKey]
        income = propertyDetail[constants.netIncomeKey]
        line = str(year) + "\t" + address
        
        for value in income:
            line += "\t" + str(value)
            
        print(line)