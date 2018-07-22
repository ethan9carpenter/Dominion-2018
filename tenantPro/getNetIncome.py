from lxml import html
from tenantPro import constants

def getNetOperatingIncome(link):
    """Return a dictionary with the key being constants.netIncomeKey and the element
    is a list of floats of the monthly net operating income for a given property"""
    
    element = getNetOperatingRow(link)
    
    for i in range(len(element)):
        element[i] = element[i].strip().replace(",", "") #Remove end spaces and commas to convert to float
        element[i] = getFloatFromAccounting(element[i]) #convert to float
        
    return {constants.netIncomeKey: element}

def getFloatFromAccounting(accountingString):
    #Convert to a negative number if surrounded by parentheses        
    if accountingString.find("(") >= 0:
        copy = accountingString
        copy = copy.replace("(", "")
        copy = copy.replace(")", "")
        accountingString = -float(copy)
    
    return float(accountingString)

def getNetOperatingRow(link):
    """Return a tidy row of the monthly net operating income."""
    with open(link, "r") as file:
        contents = file.read()
        
    root = html.fromstring(contents)
    root.xpath('//tr/td//text()')
    
    row = root.xpath('//table')[-2] #Select row of net monthly income
    element = row.xpath('.//tr/td//text()')
    
    while " " in element:
        element.remove(" ")
    element = element[1:-1] #Trim to monthly data only
    
    return element

def getKey(link):
    #Remove everything before address and trailing spaces
    info = link.split("12 Mo Summary Op Stmt for")[-1].strip()
    info = info.replace("for property ", "")
    year = 2000 + int(info[4:6]) #Parse year
    address = info[7:-4] #Parse address
    
    return {constants.yearKey: year, constants.addressKey: address}

def getList(link):
    """Return a dictionary, containing the address, year, and list of
    net operating incomes by month.  The key for each element is the corresponding
    one in constants.py"""
    
    key = getKey(link)
    content = getNetOperatingIncome(link)
    
    key.update(content)

    return key