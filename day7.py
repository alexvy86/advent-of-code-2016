"""Solution to the puzzles of day 7 of Advent of Code"""

import utils
import regex as re
from collections import deque
import itertools

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

def extract_abas(ip):
    # Replace the hypernets (between brackets []) with spaces, and split the remainder to get the supernets
    supernets = re.sub(r'\[([^\]]*)\]', ' ', ip).split()
    for supernet in supernets:
        # Use named group in regex to enforce match between first and third characters
        for aba_group in re.findall(r'((?P<a>[a-z])[a-z](?P=a))', supernet, overlapped=True):
            yield aba_group[0] # [0] because we're capturing 2 groups, the whole match and the first letter

def supports_ssl(ip):
    #print(ip)
    abas = list(extract_abas(ip))
    #print(abas)
    if len(abas) == 0: return False
    pattern = '|'.join(x[1] + x[0:2] for x in abas)
    hypernets = re.findall(r'\[([^\]]*)\]', ip)
    #print(hypernets)
    bab_matches = [match for hypernet in hypernets for match in re.findall(pattern, hypernet, overlapped=True)]
    #print(bab_matches)
    return len(bab_matches) > 0

print(len([ip for ip in utils.read_file(7).read().split() if supports_tls(ip)]))
print(len([ip for ip in utils.read_file(7).read().split() if supports_ssl(ip)]))
