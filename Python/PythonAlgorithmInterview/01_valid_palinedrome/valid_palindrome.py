#!/usr/bin/env python3
"""
Author: ckyqjy <ckyqjy@gmail.com>
Purpose: Check Valid Palindrome
"""

import argparse
import re

# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        usage='valid_palindrome.py [-h] sentence',
        description='Check if the input sentence is palindrome',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sentence',
                        metavar='sentence',
                        help='A sentence')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Main function starts here """

    args = get_args()
    sentence = ''.join(filter(str.isalpha, args.sentence.replace(" ", "")))
    length = len(sentence)
    split1 = sentence[0:length // 2]
    split2 = sentence[(length // 2) + 1:length] 
    if (split1.lower() == ''.join(split2[::-1].lower())):
        print('True')
    else:
        print('False')

# --------------------------------------------------
if __name__ == '__main__':
    main()