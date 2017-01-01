"""Solution to the puzzles of day 2 of Advent of Code"""

import utils

keypad = str.split("""
123
456
789
""")

assert keypad[1][1] == '5'

def decode(instructions, x=1, y=1):
    for next_instructions in instructions:
        for c in next_instructions:
            if   c == "U": y = max(0, y-1)
            elif c == "D": y = min(y+1, len(keypad)-1)
            elif c == "L": x = max(0, x-1)
            elif c == "R": x = min(x+1, len(keypad[0])-1)
        yield keypad[y][x]

assert ''.join(decode("URDRRRR DDL".split())) == "68"

print(''.join(decode(utils.read_file(2).readlines())))
