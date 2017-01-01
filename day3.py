
"""Solution to the puzzles of day 3 of Advent of Code"""

import utils

sides_list = [[int(x) for x in input_line.split()] for input_line in utils.read_file(3).readlines()]
sides_list_1 = [x for x in sides_list if x[0]+x[1] > x[2] and x[0]+x[2] > x[1] and x[1]+x[2] > x[0]]
print(len(sides_list_1))

sides_list_2 = [item for sublist in zip(*sides_list) for item in sublist]
group_size = 3
grouped = [sides_list_2[i:i + group_size] for i in range(0, len(sides_list_2), group_size)]
grouped = [x for x in grouped if x[0]+x[1] > x[2] and x[0]+x[2] > x[1] and x[1]+x[2] > x[0]]
print(len(grouped))
