#!python3

import requests, pyperclip, datetime, json, prettytable, sys
from bs4 import BeautifulSoup

def retrievedDataFromBiliBili():
    url = 'https://www.bilibili.com/bangumi/media/md5267730/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    stats = soup.select('.media-info-datas')[0].text.replace('万', '').split()
    d = datetime.datetime.now()
    resultDict = {
        f'{d}' : {
        'Date' : f'{d.date()}',
        'Time' : f'{d.hour}',
        'Stats' : {
            'Total views' : f'~{int(float(stats[1])*10000)}',
            'Following' : f'~{int(float(stats[3])*10000)}',
            'Total floating comments' : f'~{int(float(stats[5])*10000)}',
            'Score' : f'{stats[6]}',
            'Total number of ratings' : f'{stats[7]}'
            }
        }
    }
    return resultDict

def writeToJSON(stat):
    with open('kaguyaB.json', 'r') as f:
        data = json.load(f)

    data.update(stat)

    with open('kaguyaB.json', 'w') as f:
        json.dump(data, f)

def constructTable():
    pt = prettytable.PrettyTable()
    pt.field_names = ['Date', 'Time', 'Views', 'Following', 'Danmaku', 'Score', 'Raters']

    with open('kaguyaB.json', 'r') as f:
        data = json.load(f)

    for entry in data:
        pt.add_row([data[entry]['Date'], data[entry]['Time'], data[entry]['Stats']['Total views'], data[entry]['Stats']['Following'], data[entry]['Stats']['Total floating comments'], data[entry]['Stats']['Score'], data[entry]['Stats']['Total number of ratings']])
    
    return pt

def newEntry():
    writeToJSON(retrievedDataFromBiliBili())
    print(constructTable())
    pyperclip.copy(f'```Stats on BiliBili: \n{constructTable()}```')

def pastEntries():
    print(constructTable())
    pyperclip.copy(f'```Stats on BiliBili: \n{constructTable()}```')

try:
    if sys.argv[1] == 'new' or sys.argv[1] == 'n':
        newEntry()
    else:
        pastEntries()
except IndexError:
    print('Invalid system argument. Enter "new" or "history".')