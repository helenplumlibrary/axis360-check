import sys
import os.path
import requests
import pandas as pd

baseUrl = 'http://plum.axis360.baker-taylor.com/Title?itemid='

def getKeys(fileName):
    try:
        data = pd.read_excel(fileName, dtype={'BTKey': object})
        keys = data['BTKey'] # Get BTKeys from Excel data
        keys = list(set(keys)) # Deduplicate list
    except:
        print('ERROR: Failed to ready data from file "{}"'.format(fileName))
        exit()
    return keys

def checkKeys(keys):
    print('# Searching for invalid title keys...')
    print('Title keys not found in the library\'s Axis360 collection will be listed below:')
    for key in keys:
        url = baseUrl + key
        response = requests.get(url)
        if 'Error 404 Title Not Found' in response.text:
            print(key)
    print('# Search complete')

if __name__ == "__main__": 
    fileName = sys.argv[1]
    if os.path.isfile(fileName):
        keys = getKeys(fileName)
        checkKeys(keys)
    else:
        print('ERROR: File "{}" not found'.format(fileName))
    