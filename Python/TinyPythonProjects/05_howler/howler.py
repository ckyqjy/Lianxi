#!/usr/bin/env python3
"""
Author: ckyqjy <ckyqjy@gmail.com>
Purpose: Manipulate Python file I/O
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        usage='howler.py [-h] [-o str] text',
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o', '--outfile',
                        action='store',
                        help='Output filename',
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def parse_args(args):
    """ Parse args and R/W file """
    text = args.text
    out = args.outfile

    if (os.path.isfile(text)):
        text = open(text).read().rstrip()

    if (out):
        if ('.txt' in out):
            out_fh = open(out, 'wt')
            out_fh.write(text.upper())
            out_fh.close()

            return ''

    return text


# --------------------------------------------------
def main():
    """ Main function starts here """

    args = get_args()
    items = parse_args(args)
    
    if (items != ''):
        print(items.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()