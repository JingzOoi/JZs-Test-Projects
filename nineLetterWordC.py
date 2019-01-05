#! python3
# nineLetterWordC.py: Cheat even in this easy game: https://nineletterword.tompaton.com/
# Usage: [1] Launch the script: >>> python nineLetterWordC.py <yourHand>
# Requirements: requests, bs4
# Note: if it says 'Already guessed', it's normal. Another word with the same combination has already been guessed.

import requests, sys
from bs4 import BeautifulSoup

try:
    url = 'https://nineletterword.tompaton.com/' + sys.argv[1].upper()
except IndexError:
    print('Missing Argument! Make sure you pass your Hand as an argument.')
    exit()

if len(sys.argv[1]) == 9:
    print('Calculating...')
else:
    print('Invalid Hand! Make sure the Hand contains exactly nine (9) letters.')
    exit()

try:
    page = requests.get(url)
    page.raise_for_status()

    soup = BeautifulSoup(page.text, 'lxml')
    script = soup.select('script')[1].text.split('[')[2].split(']')[0]
    answer = script.split(',')

    answerList = []
    i = 0
    for n in answer:
        out = n.strip().strip('"')
	i += 1
	print('[{}] '.format(i) + out)
        answerList.append(out)

    print('There are% d possible answers.' % len(answerList))

except:
    print('An error has occured. Check if:\n[1] the device is connected to the Internet, or\n[2] The requirements are installed correctly.')
