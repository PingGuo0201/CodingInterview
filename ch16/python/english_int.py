#!/usr/bin/env python

'''
Author: Ping Guo
Email: TODO
Problem Statement:
    Given any integer, print an English phrase that describes (e.g. One
    Thousand, Two Hundred Thirty Four)
Complexity: TODO
Usage: english_int <int>
'''


def threeDigit(s):
	'''
    when given a three digit number, print an english phrase. (e.g. Five Hundred
    Forty Three)
    '''
    dictOne = {'1': 'One',
               '2': 'Two',
               '3': 'Three',
               '4': 'Four',
               '5': 'Five',
               '6': 'six',
               '7': 'Seven',
               '8': 'Eight',
               '9': 'Nine'
            }
	dictTwo = {'10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen',
                '14': 'Fourteen', '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen'}
    dictThree = {'2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty', '6': 'Sixty', '7': 'Seventy',
                     '8': 'Eighty',  '9': 'Ninety'}


    phrase = ''
    if s[0] is in dictOne:
    	phrase = phrase + dictOne.get(s[0]) + ' Hundred'


    if s[1:3] is in dictTwo:
    	phrase = phrase + dictTwo.get(s[2:4])
    elif s[1] is in dictThree:
    	phrase = phrase + dictThree.get(s[1]) + dictOne.get(s[2])

    return phrase

def answer(n):
    dictFour = {'4': 'Thousand',
                '7': 'Million',
                '10': 'Billion',
                '13': 'Trillion',
                '16': 'Quadrillion',
                '19': 'Quintillion',
                }
	numString = str(n)
	strLen = len(numString)
    i = strLen -3
    f_phrase = ''
    if i >= 0:
        if numString[i:i+3] != '000':
            f_phrase = threeDigit(numString[i:i+3]) + dictFour.get('strLen-i')+ f_phrase
        i = i -3
    else:
        i = i +3
        f_phrase = threeDigit(numString[0:i]) + dictFour.get('strLen-i')+ f_phrase

    return f_phrase


# executable
if __name__ == '__main__':
    # executable import only
    from docopt import docopt

    args = docopt(__doc__)

    n = int(args['<int>'])

    print answer(n)
