"""Solution to the puzzles of day 6 of Advent of Code"""

import utils
import itertools

messages = list(map(list, utils.read_file(6).readlines()))

transposed = list(zip(*messages))
real_message = (sorted(char_list) for char_list in transposed)
real_message = ([(k, len(list(g))) for k, g in itertools.groupby(x)] for x in real_message)
real_message = ((sorted(x, key=lambda y: -y[1]))[0] for x in real_message)
real_message = (x[0] for x in real_message)
print(''.join(list(real_message)))
