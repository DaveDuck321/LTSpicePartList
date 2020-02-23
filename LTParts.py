#!/usr/bin/env python3

import sys
from collections import defaultdict

def exit_msg(code, *lines):
    for line in lines:
        print(line, file=sys.stderr)
    exit(code)

def print_parts(parts):
    parts = list(sorted(zip(parts.values(), parts.keys()), reverse=True))
    longest_name = max(map(
        lambda part: len(part[1][0]),
        parts
    ))

    longest_value = max(map(
        lambda part: len(part[1][1]),
        parts
    ))

    row = f"| {{:<{longest_name}}} | {{:<{longest_value}}} | {{:<5}} |"

    print(row.format("Name", "Value", "Count"))
    print("-" * len(row.format("", "", "")))

    for (count, (name, value)) in parts:
        print(row.format(name, value, count))

def append_parts(parts, file):
    current_symbol = None

    for line in file.readlines():
        command = line.split(' ')
        if command[0] == 'SYMBOL':
            if current_symbol:
                parts[current_symbol] += 1
            current_symbol = (command[1], '')
        if command[0] == 'SYMATTR':
            if command[1] == 'Value':
                current_symbol = (current_symbol[0], command[2].strip())

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 1:
        exit_msg(1, "Error: Incorrect usage", "Please use: LTParts file.asc")

    parts = defaultdict(int)
    try:
        for file in args:
            append_parts(parts, open(args[0], 'r'))

        print_parts(parts)
    except IOError:
        exit_msg(2, "Error: File system", f"File {file} could not be opend")