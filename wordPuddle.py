#! python3
# wordPuddle3: Word game answer finder.
# Word game: Given a string of a length of an odd number, the player must form valid words, each containing the middlemost letter.
# Usage: [1] Run the script: >>> python3 wordPuddle.py
#        [2] When prompted, enter your Hand. 
# Note: the longer your Hand is, the longer it takes to process, but it differs with device specs.
# For reference, a 9-letter word took 1701 seconds to be run for me with 985,824 iterations.
# Additional modules: requests

import itertools, requests, timeit

print('\nConnecting to wordlist...')

url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt' # online source for wordlist
page = requests.get(url)
page.raise_for_status()

# splits up text in source into a list of words
wordList = page.text.lower().split()

hand = input('Connected to wordlist. \nInsert your Hand here: ').lower()

# checks if the Hand has an odd length
if len(hand) % 2 != 1:
    print('The Hand should be of a length with an odd number. Check your Hand and try again.')
    exit()

# starts timer
print('\nStarting operations. Timer starts now.')
startTime = timeit.default_timer()

# identifies letter in the middle. iLetter(tm).
iLetter = hand[len(hand)//2]

validList = []
i = 0

# basically brute forces the words with combinations of letters
for count in range(4, len(hand)+1):
    for comb in itertools.permutations(hand, count):
        combination = ''.join(comb)
        i += 1
        if (combination in wordList) and (iLetter in combination) and (combination not in validList):
            validness = 'Valid'
            validList.append(combination)
        else:
            validness = 'Invalid'

        # words to be printed when operations are running. Mostly for visual effects.
        load = '[{}] Generated word {}: {} | {} valid words found.'.format(i, combination, validness.rjust(7), len(validList))
        print(load, end='')
        print('\b'*len(load), end='', flush=True)

endTime = timeit.default_timer()
c = 0
print('\n-----Matching operations ended-----\n\n-----Displaying results-----\nValid words:')
for valid in validList:
    c += 1
    print('[{}] '.format(c) + valid)
print('-----End of results-----\n\nOut of {} iterations created, {} are valid. \nA total of {} seconds were used.\n'.format(i, c, round(endTime-startTime, 3)))