"""Solution to the puzzles of day 4 of Advent of Code"""

import utils
import re
import itertools

def checksum(room_name):
    room_name = room_name.replace('-', '')
    grouped = [(k, list(g)) for k, g in itertools.groupby(sorted(room_name))]
    grouped.sort(key=lambda x: -len(x[1]))
    return ''.join(x[0] for x in grouped[:5])

assert checksum("aaaaa-bbb-z-y-x") == "abxyz"
assert checksum("a-b-c-d-e-f-g-h") == "abcde"
assert checksum("not-a-real-room") == "oarel"

def is_valid_room(regex_groups):
    return checksum(regex_groups[0]) == regex_groups[2]

rooms = utils.read_file(4).readlines()
processed_rooms = [re.match(r'(.+)-(\d+)\[(.+)\]', room).groups() for room in rooms]
print(sum(int(x[1]) for x in processed_rooms if is_valid_room(x)))
