#! python3
# scrabbleSearcher.py: Cheat at Scrabble with minimal effort!
# Usage: [1] Run the script: python scrabbleSearcher.py
#        [2] The output shows a list of the possible valid combinations and the scores they take. (No special tiles)
#        [3] DON'T TALK ABOUT HOW THERE'S NO BLANK CARD AHHHHHHHH
# Requirements: @adambom's dictionary json file at https://github.com/adambom/dictionary
# Notes: Repetition of words in the list should be normal because different letter recognition, etc.

import itertools, json

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

word = input('Insert your hand here: ').upper()

with open('dictionary.json', encoding='utf-8') as json_data:
    dictionary = json.load(json_data)

i = 0
for count in range(2,8):
    for comb in itertools.permutations(word, count):
        score = 0
        for letter in comb:
            score += LETTER_VALUES[letter]
        
        combination = ''.join(comb)

        try:
            definition = dictionary[combination]
            print('[{}] {}'.format(score, combination))
            i += 1
        except KeyError:
            continue

print('A total of %d combinations are available.' % i)