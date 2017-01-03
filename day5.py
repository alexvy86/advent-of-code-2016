"""Solution to the puzzles of day 4 of Advent of Code"""

import hashlib

def get_password_characters(door_id, password_length):
    """Looks for the first 'password_length' characters of the password corresponding to 'door_id'
    and returns them one by one"""
    gen_char_count = 0
    i = 0
    while gen_char_count < password_length:
        hashed = hashlib.md5("{0}{1}".format(door_id, i).encode('utf-8')).hexdigest()
        if hashed[0:5] == "00000":
            gen_char_count += 1
            yield (i, hashed[5])
        i += 1

puzzle_input = "ugkcyxxp"
password_characters = [x for x in get_password_characters(puzzle_input, 8)]
print(password_characters)
# [(702868, 'd'), (1776010, '4'), (8421983, 'c'), (8744114, 'd'), (8845282, '2'), (9268910, 'e'), (9973527, 'e'), (10253166, '1')]
