#!/usr/bin/env python3
"""
Author: ckyqjy <ckyqjy@gmail.com>
Purpose: Manipulate multiple args
"""

import argparse

# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        usage='picnic.py [-h] words',
        description='Print multiple args with picnic format',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('words',
                        metavar='words',
                        nargs='+',
                        help='Words')

    parser.add_argument('-s', '--sorted',
                        action='store_true',
                        help='Sort the arguments')

    parser.add_argument('-n', '--nocomm',
                        action='store_true',
                        help='Delete the last comma')

    parser.add_argument('-o', '--option',
                        action='store',
                        help='Change the seperator',
                        default=',')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Main function starts here """

    args = get_args()
    words = args.words
    length = len(words)
    items = ''

    if args.sorted:
        words.sort()

    if length == 1:
        items = words[0]
    elif length == 2:
        items = ' and '.join(words)
    else:
        if args.nocomm:
            split = words[length - 2:length]
            split[-1] = 'and ' + split[-1]
            words = words[0:length - 2]
            items = f'{args.option} '.join(words) + f'{args.option} '
            items += ' '.join(split)
        else:
            words[-1] = 'and ' + words[-1]
            items = f'{args.option} '.join(words)
        
    print(f'You are bringing {items}')


# --------------------------------------------------
if __name__ == '__main__':
    main()