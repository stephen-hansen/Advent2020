from utils import *
import re
import copy
from functools import *
from collections import *

def get_regex(rid, rules_map):
    pattern = ''
    rule = rules_map[rid]
    if rid == 8:
        return '(' + get_regex(42, rules_map) + '+' + ')'
    elif rid == 11:
        # just bruteforce, input is never that big
        pairings = []
        a = get_regex(42, rules_map)
        b = get_regex(31, rules_map)
        for q in range(1, 25):
            pairings.append(a * q + b * q)
        return '(' + '|'.join(pairings) + ')'
    if isinstance(rule, str):
        return rule
    pairings = []
    for pair in rule:
        pairing = ''
        for i in pair:
            pairing += get_regex(i, rules_map)
        pairings.append(pairing)
    return '(' + '|'.join(pairings) + ')'

def match(line, rid, rules_map):
    rule = rules_map[rid]
    regex = re.compile(get_regex(rid, rules_map))
    return bool(re.fullmatch(regex, line))

def main():
    # Load all lines
    lines = getlines()
    rules = True
    rules_map = {}
    regex = None
    c = 0
    for l in lines:
        p(l)
        if l == '':
            rules = False
            regex = re.compile(get_regex(0, rules_map))
        elif rules:
            pat = re.compile(r'(\d+): (.*)')
            m = re.fullmatch(pat, l)
            rid = int(m.group(1))
            to = m.group(2)
            if to[0] == '"':
                rules_map[rid] = to[1]
            else:
                pairs = to.split('|')
                rules_map[rid] = []
                for pi in pairs:
                    nums = list(map(int, pi.strip().split(' ')))
                    rules_map[rid].append(nums)
        else:
            c += bool(re.fullmatch(regex, l))

    p(c)

if __name__ == '__main__':
    main()
