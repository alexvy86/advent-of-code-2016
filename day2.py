"""Solution to the puzzles of day 2 of Advent of Code"""

import utils

keypad = str.split("""
.....
.123.
.456.
.789.
.....
""")

keypad2 = """
.......
...1...
..234..
.56789.
..ABC..
...D...
.......
""".split()

assert keypad[2][2] == '5'
assert keypad2[3][1] == '5'

def decode(instructions, keypad, x, y):
    for next_instructions in instructions:
        for c in next_instructions:
            if   c == "U" and keypad[y-1][x] != '.': y -= 1
            elif c == "D" and keypad[y+1][x] != '.': y += 1
            elif c == "L" and keypad[y][x-1] != '.': x -= 1
            elif c == "R" and keypad[y][x+1] != '.': x += 1
        yield keypad[y][x]

assert ''.join(decode("URDRRRR DDL".split(), keypad, 2, 2)) == "68"

print(''.join(decode(utils.read_file(2).readlines(), keypad, 2, 2)))

print(''.join(decode(utils.read_file(2).readlines(), keypad2, 3, 1)))
