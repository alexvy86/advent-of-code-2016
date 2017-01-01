"""Solution to the puzzles of day 1 of Advent of Code"""

from collections import namedtuple
import utils

NORTH, EAST, SOUTH, WEST = range(4)

Point = namedtuple("Point", "x y")

def manhattan_distance(point1, point2=Point(0, 0)):
    """Returns the Manhattan distace between 2 Points"""
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

assert manhattan_distance(Point(0, 0), Point(0, 0)) == 0
assert manhattan_distance(Point(0, 0), Point(1, 1)) == 2
assert manhattan_distance(Point(-2, -2), Point(2, 2)) == 8

def follow_steps(steps, location=Point(0, 0), direction=NORTH):
    """Returns two Points; the first one indicates the ending location based on the sequence
    of steps, and the second one  indicates the first location to be visited twice"""
    visited = set(location)
    first_visited_twice = None
    for step in steps:
        direction = (direction - 1 if step[0] == 'L' else direction + 1) % 4
        distance = int(step[1:])
        for i in range(distance):
            if direction == NORTH:
                location = Point(location.x, (location.y + 1))
            elif direction == SOUTH:
                location = Point(location.x, (location.y - 1))
            elif direction == EAST:
                location = Point((location.x + 1), location.y)
            else:
                location = Point((location.x - 1), location.y)
            if first_visited_twice == None and location in visited:
                first_visited_twice = location
            visited.add(location)
    return location, first_visited_twice

input_data = utils.read_file(1).read()
steps = input_data.replace(' ', '').split(',')

final_location, first_visited_twice = follow_steps(steps)
print(manhattan_distance(final_location))
print(manhattan_distance(first_visited_twice))
