import csv, re
from constants import *
from address import Address

def loadAddresses(filePath):
    addresses = {}
    
    with open(filePath) as file:
        for row in csv.reader(file):
            row = row[0].lower()
            addresses[row] = row
    
    return addresses

def getNumber(address):
    address = address.replace('1/2', '.5')
    
    number = re.split('[a-z]+', address)[0]
    
    if number.find('.5') >= 0:
        number = number.replace(' ', '')
    else:
        number = re.split(' ', number)[0]
    
    try:
        number = int(number)
    except Exception:
        number = float(number)
        
    return number

def replaceStreetType(street):
    lastWord = street[-1]
    
    if lastWord in streetTypeKey:
        street[-1] = streetTypeKey[lastWord]
    elif str(street[-1])+'.' in streetTypeKey:
        street[-1] = streetTypeKey[lastWord+'.']
    return street

def replaceSpecialType(street):
    for i, word in enumerate(street):
        if word in specialKey:
            street[i] = specialKey[word]
        elif str(word)+'.' in specialKey:
            street[i] = specialKey[word+'.']

def removeFromAddress(street):
    newStreet = []
    for word in street:
        if word not in toRemove and str(word)+'.' not in toRemove:
            newStreet.append(word)
    
    return newStreet

def removeNumber(street):    
    for i, part in enumerate(street):
        try:
            float(part)
            street[i] = ''
        except Exception:
            continue
    return street

def getAndRemoveUnit(street):
    index = None
    for i, part in enumerate(street):
        if 'unit' in part or '#' in part:
            index = i
            break
        
    if not index:
        return street, None
    else:   
        unit = street[i:]
        newStreet = street[:i]
        
        unit = parseUnit(unit)
        
        return newStreet, unit

def parseUnit(unit):
    newUnit = ""
    for part in unit:
        if 'unit' not in part:
            for character in part:
                if character != '#':
                    newUnit += character
        newUnit += " "
    unit = newUnit
    
    return unit

def getStreetAndUnit(address):
    street = re.split(' ', address)
    removeNumber(street)
    
    street, unit = getAndRemoveUnit(street)   

    street = removeFromAddress(street)
    replaceStreetType(street)
    replaceSpecialType(street)
    
    streetString = street[0]
    
    for part in street[1:]:
        streetString += " " + part
    
    return streetString, unit

def getAddressMap(filePath):
    addresses = loadAddresses(filePath)
    
    for address in addresses.keys():
        number = getNumber(address)
        street, unit = getStreetAndUnit(address)
        
        stylizedAddress = Address(number, street, unit=unit)
        addresses[address] = stylizedAddress
    
    return addresses
   
    
    