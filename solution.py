#!/usr/bin/env python3
import sys
import os

from input import parse_input


def process_data(data):
    print('processing data')
    return None

def produce_output(output):
    print('Hello World!')


def main():
    data = parse_input(os.path.join('/home/cgalvezd/git/hashcode-2018', 'data','a_example.in'))
    #output = process_data(data)
    #produce_output(output)

if __name__ == '__main__':
    main()
