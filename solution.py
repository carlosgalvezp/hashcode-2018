#!/usr/bin/env python3
import sys
import os

from input import parse_input
from output import create_output


def main():
    data = parse_input(os.path.join('/home/cgalvezd/git/hashcode-2018', 'data','b_should_be_easy.in'))
    solution = create_output(data)
    print(solution)

    #produce_output(output)

if __name__ == '__main__':
    main()
