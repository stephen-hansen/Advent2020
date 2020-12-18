from utils import *
import re
import copy
from functools import *
from collections import *

def evaluate(math):
    if math.isnumeric():
        return int(math)
    i1 = None
    i2 = None
    op = None
    scope = 0
    i = len(math)
    while i > 0:
        i -= 1
        c = math[i]
        if c == ')':
            scope += 1
        elif c == '(':
            scope -= 1
        elif c == '*' and scope == 0:
            op = '*'
            i1 = math[:i]
            i2 = math[i+1:]
    
    if op is None:
        i = len(math)
        scope = 0
        while i > 0:
            i -= 1
            c = math[i]
            if c == ')':
                scope += 1
            elif c == '(':
                scope -= 1
            elif c == '+' and scope == 0:
                op = '+'
                i1 = math[:i]
                i2 = math[i+1:]
    if op == '+':
        return evaluate(i1) + evaluate(i2)
    elif op == '*':
        return evaluate(i1) * evaluate(i2)
    else:
        return evaluate(math[1:len(math)-1])

def main():
    # Load all lines
    lines = getlines()
    s = 0
    for l in lines:
        r = evaluate(l.replace(" ", ""))
        p(r)
        s += r
    p(s)
            
if __name__ == '__main__':
    main()
