"""Solution to the puzzles of day 5 of Advent of Code"""

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

def get_partial_passwords(door_id, password_length):
    """Calculates the 'password_length' positions of the password corresponding to 'door_id'
    and returns the partial passwords as it does"""
    current_password = list("_" * password_length)
    i = 0
    while "_" in current_password:
        hashed = hashlib.md5("{0}{1}".format(door_id, i).encode('utf-8')).hexdigest()
        if hashed[0:5] == "00000":
            try:
                position = int(hashed[5])
            except:
                position = password_length # Make it an invalid position if it can't be parsed    
            if position < password_length and current_password[position] == "_":
                current_password[position] = hashed[6]
                yield ''.join(current_password)
        i += 1

puzzle_input = "ugkcyxxp"
password_characters = [x for x in get_password_characters(puzzle_input, 8)]
print(password_characters)
# [(702868, 'd'), (1776010, '4'), (8421983, 'c'), (8744114, 'd'), (8845282, '2'), (9268910, 'e'), (9973527, 'e'), (10253166, '1')]

for current_password in get_partial_passwords(puzzle_input, 8):
    print(current_password)
# f2c730e5