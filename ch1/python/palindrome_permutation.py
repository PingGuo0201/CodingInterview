#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Problem Statement:
    Given a string, write a function to check if it is a permutation of a
    palindrome. A palindrome is a word or phrase that is the same forwards as
    backwards. A permutation is a rearrangement of letters. The palindrome
    does not need to be limited to just dictionary words.

    EXAMPLE
    Input:      Tact Coa
    Output:     True (permutations: "taco cat", "atco cta", etc.)
Complexity: TODO
Usage:
    palindrome_permutation <word>
'''


def answer(word):
    '''
    Function to parse string to see if it is a palindrome.
    '''
    # get word length
    lw = len(word)

    # determine length odd/even
    if lw % 2:
        odd = True
    else:
        odd = False

    # create dict
    char_dict = {}

    # fill dict
    for c in word:
        try:
            char_dict[c] += 1
        except KeyError:
            char_dict[c] = 1

    # scan dict
    count = 0
    for key, val in char_dict.iteritems():
        if val % 2 and not odd:
            return False
        elif val % 2 and odd:
            if count > 1:
                return False
            else:
                count += 1
    return True


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # execute
    print answer(args['<word>'])
