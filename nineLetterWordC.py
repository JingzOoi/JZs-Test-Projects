#! python3
# nineLetterWordC.py: Cheat even in this easy game: https://nineletterword.tompaton.com/
# Usage: [1] Launch the script: >>> python nineLetterWordC.py <yourHand>
# Requirements: requests, bs4, selenium, geckodriver
# Note: if it saya 'Already guessed', it's normal. Another word with the same combination has already been guessed.

import requests, sys
from bs4 import BeautifulSoup
from selenium import webdriver

try:
    url = 'https://nineletterword.tompaton.com/' + sys.argv[1]
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

    for n in answer:
        out = n.strip().strip('"')
        answerList.append(out)

    print('There are% d possible answers.\nLaunching browser...' % len(answerList))

    driver = webdriver.Firefox()
    driver.get(url)

    guess = driver.find_element_by_class_name('guess')
    btnGuess = driver.find_element_by_class_name('move')

    for i in range(len(answerList)):
        guess.send_keys(answerList[i])
        btnGuess.click()
        print('[{}] Trying '.format(i+1) + answerList[i] + '...')

    validList = driver.find_elements_by_class_name('right')
    print('Completed. \nOut of {} possible answers, {} are valid.\nYou can close the browser now.'.format(len(answerList), len(validList)))

except:
    print('An error has occured. Check if:\n[1] the device is connected to the Internet, or\n[2] The requirements are installed correctly.')