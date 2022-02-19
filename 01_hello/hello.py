#!/usr/bin/env python3
"""
Author: ckyqjy <ckyqjy@gmail.com>
Purpose: Say Hello
"""

import argparse

def get_args():
    """ Get the command-line arguments """
    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    return parser.parse_args()

def main():
    """ Main function starts here """
    args = get_args()
    print("Hello, " + args.name + "!")

if __name__ == '__main__':
    main()