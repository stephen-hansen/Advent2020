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
    while i1 is None:
        i -= 1
        c = math[i]
        if i2 is None:
            if c.isnumeric():
                i2 = c
            else:
                scope = 1
                while scope > 0:
                    i -= 1
                    c = math[i]
                    if c == ')':
                        scope += 1
                    elif c == '(':
                        scope -= 1
                i2 = math[i+1:len(math)-1]
                if '(' + i2 + ')' == math:
                    return evaluate(i2)
        elif op is None:
            op = c
        else:
            i1 = math[0:i+1]
    p(i1 + op + i2)
    p('---')
    if op == '+':
        return evaluate(i1) + evaluate(i2)
    elif op == '*':
        return evaluate(i1) * evaluate(i2)

def main():
    # Load all lines
    lines = getlines()
    s = 0
    for l in lines:
        r = evaluate(l.replace(" ", ""))
        #p(r)
        s += r
    p(s)
            
if __name__ == '__main__':
    main()
