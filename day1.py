"""Solution to the puzzles of day 1 of Advent of Code"""

from collections import namedtuple
import utils

NORTH, EAST, SOUTH, WEST = range(4)

Point = namedtuple("Point", "x y")

def manhattan_distance(point1, point2):
    """Returns the Manhattan distace between 2 Points"""
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

assert manhattan_distance(Point(0, 0), Point(0, 0)) == 0
assert manhattan_distance(Point(0, 0), Point(1, 1)) == 2
assert manhattan_distance(Point(-2, -2), Point(2, 2)) == 8

def puzzle1():
    """Solve puzzle 1"""
    input_data = utils.read_file(1).read()
    location, direction = Point(0, 0), NORTH
    steps = input_data.replace(' ', '').split(',')
    print(steps)
    for step in steps:
        direction = (direction - 1 if step[0] == 'L' else direction + 1) % 4
        distance = int(step[1:])
        if direction == NORTH:
            location = Point(location.x, (location.y + distance))
        elif direction == SOUTH:
            location = Point(location.x, (location.y - distance))
        elif direction == EAST:
            location = Point((location.x + distance), location.y)
        else:
            location = Point((location.x - distance), location.y)
    print(manhattan_distance(Point(0, 0), location))

puzzle1()
