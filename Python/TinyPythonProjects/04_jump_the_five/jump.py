#!/usr/bin/env python3
"""
Author: ckyqjy <ckyqjy@gmail.com>
Purpose: Manipulate Python dictionary
"""

import argparse

# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        usage='jump.py [-h] str',
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def parse_args(args):
    """ Parse args using Jump the Five cipher """
    dict = {'1':'9', '2':'8', '3':'7', '4':'6', '5':'0', '6':'4', '7':'3', '8':'2', '9':'1', '0':'5' }

    # my answer
    # input = list(args.str)
    # for idx, char in enumerate(input):
    #     if char.isdigit():
    #         input[idx] = dict[char]
    # return (''.join(input))

    # recommanded answer
    # answer 1:
    # new_text = ''
    # for char in args.text:
    #     new_text += dict.get(char, char)
    # return new_text

    # answer 2:
    # return (''.join([dict.get(char, char) for char in args.str]))

    # answer 3:
    return (args.str.translate(str.maketrans(dict)))


# --------------------------------------------------
def main():
    """ Main function starts here """

    args = get_args()
    items = parse_args(args)
        
    print(items)


# --------------------------------------------------
if __name__ == '__main__':
    main()