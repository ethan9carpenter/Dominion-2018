from tenantPro import getNetIncome
import os

def getAllIncome(year):
    directory = getAllFilePaths(year)
    properties = []
    errors = []
    
    for path in directory:
        try:
            properties.append(getNetIncome.getList(path))
        except ValueError:
            errors.append(path)
    if errors:
        print("Errors retreiving data from:")
        for path in errors:
            print("\t" + path)   
    
    return properties

def getAllFilePaths(year):
    basePath = "/Users/footballnerd12/desktop/tenantProHTML/" + str(year)
    directory = os.listdir(basePath)
    
    for i in range(len(directory)):
        directory[i] = basePath + "/" + directory[i]
        
    return directory
