#!/usr/bin/env python3
import sys
import os

from input import parse_input
from output import create_output


def main():
    filepath = sys.argv[1]
    data = parse_input(filepath)
    solution = str(create_output(data))
    print(solution[:-1])

if __name__ == '__main__':
    main()
