#!/usr/bin/env python3

import sys

def exit_msg(code, *lines):
    for line in lines:
        print(line, file=sys.stderr)
    exit(code)

def print_parts(parts):
    pass

def append_parts(parts, file):
    pass

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 1:
        exit_msg(1, "Error: Incorrect usage", "Please use: LTParts file.asc")

    parts = {}
    try:
        for file in args:
            append_parts(parts, open(args[0], 'r'))

        print_parts(parts)
    except IOError:
        exit_msg(2, "Error: File system", f"File {file} could not be opend")