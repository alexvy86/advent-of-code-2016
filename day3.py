"""Solution to the puzzles of day 3 of Advent of Code"""

import utils

sides_list = [[int(x) for x in input_line.split()] for input_line in utils.read_file(3).readlines()]
sides_list = [x for x in sides_list if x[0]+x[1] > x[2] and x[0]+x[2] > x[1] and x[1]+x[2] > x[0]]
print(len(sides_list))
