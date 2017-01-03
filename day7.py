"""Solution to the puzzles of day 7 of Advent of Code"""

import utils
from collections import deque

def supports_tls(ip):
    within_brackets = False
    running_string = deque("____")
    supports_TLS = False
    for i in list(ip):
        if i in '[]':
            within_brackets = not within_brackets
            running_string = deque("____")
        else:
            running_string.popleft()
            running_string.append(i)
            if running_string[0] == running_string[3] and running_string[1] == running_string[2] and running_string[0] != running_string[1]:
                if within_brackets: return False
                else: supports_TLS = True
    return supports_TLS

print(len([ip for ip in utils.read_file(7).read().split() if supports_tls(ip)]))

