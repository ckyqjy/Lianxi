#!/usr/bin/env python3
"""
Author: ckyqjy <ckyqjy@gmail.com>
Purpose: Check Article Type
"""

import argparse
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        usage='crowsnest.py [-h] word',
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    parser.add_argument('--starboard',
                        action='store_true',
                        help='Print starboard instead of larboard')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Main function starts here """

    args = get_args()
    word = args.word
    if re.match(r'^[a-zA-Z]+$', word) is None:
        print('Please input alphabets only')
    else:
        article = ''
        if word[0].islower():
            if word[0].lower() in 'aeiou': article = 'an'
            else: article = 'a'
        else:
            if word[0].upper() in 'AEIOU': article = 'An'
            else: article = 'A'

        board = 'starboard' if args.starboard else 'larboard'
        print(f'Ahoy, Captain, {article} {word} off the {board} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()