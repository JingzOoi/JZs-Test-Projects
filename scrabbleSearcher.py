#! python3
# scrabbleSearcher.py: Cheat at Scrabble with minimal effort!
# Usage: [1] Run the script: python scrabbleSearcher.py. When prompted, enter your Hand.
#        [2] The output shows a list of the possible valid combinations and the scores they take. (No special tiles)
#        [3] DON'T TALK ABOUT HOW THERE'S NO BLANK CARD AHHHHHHHH
# Requirements: requests

import itertools, requests, timeit

LETTER_VALUES = {"A": 1,
                 "B": 3,
                 "C": 3,
                 "D": 2,
                 "E": 1,
                 "F": 4,
                 "G": 2,
                 "H": 4,
                 "I": 1,
                 "J": 1,
                 "K": 5,
                 "L": 1,
                 "M": 3,
                 "N": 1,
                 "O": 1,
                 "P": 3,
                 "Q": 10,
                 "R": 1,
                 "S": 1,
                 "T": 1,
                 "U": 1,
                 "V": 4,
                 "W": 4,
                 "X": 8,
                 "Y": 4,
                 "Z": 10}

print('\nConnecting to wordlist...')

url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt' # online source for wordlist
page = requests.get(url)
page.raise_for_status()

wordList = page.text.lower().split()

# splits up text in source into a list of words


hand = input('Connected to wordlist. \nInsert your Hand here: ').lower()

# starts timer
print('\nStarting operations. Timer starts now.')
startTime = timeit.default_timer()


i = 0
validList = {}
for count in range(2, len(hand)+1):
    for comb in itertools.permutations(hand, count):
        score = 0
        for letter in comb:
            score += LETTER_VALUES[letter.upper()]
        combination = ''.join(comb)
        if (combination in wordList) and (combination not in validList):
            validness = 'Valid'
            validList[combination] = score
        else:
            validness = 'Invalid'
        i += 1

        # words to be printed when operations are running. Mostly for visual effects.
        load = '[{}] Generated word {}: {}'.format(i, combination, validness)
        print(load, end='')
        print('\b'*len(load), end='', flush=True)

endTime = timeit.default_timer()
c = 0
print('\n-----Matching operations ended-----\n\n-----Displaying results-----\nValid words:')
for valid in validList:
    c += 1
    print('[{}] {} - {}'.format(c, str(validList[valid]).rjust(2), valid))
print('-----End of results-----\n\nOut of {} iterations created, {} are valid. \nA total of {} seconds were used.\n'.format(i, c, round(endTime-startTime, 3)))