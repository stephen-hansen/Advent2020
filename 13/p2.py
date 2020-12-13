from utils import *
import re
import copy
from functools import *

# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def mul_inv(a,b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

def main():
    # Load all lines
    lines = getlines()
    #lines[1] = '1789,37,47,1889'
    s = lines[1].split(',')
    first = 0
    f = 0
    d = 0
    funcs = []
    start_val = int(s[0])
    for i in s:
        if i == 'x':
            d += 1
            continue
        i = int(i)
        func = (d, i)
        funcs.append(func)
        d += 1
    print(funcs)
    n = []
    a = []
    for func in funcs:
        d, i = func
        n.append(i)
        a.append(-d % i)
    # https://rosettacode.org/wiki/Chinese_remainder_theorem
    # ... wtf
    N = reduce(lambda x, y: x*y, n)
    x = 0
    print(n)
    print(a)
    for i in range(len(n)):
        ni = n[i]
        ai = a[i]
        pi = N//ni
        si = mul_inv(pi, ni)
        x += ai * si * pi
    x = x % N
    p(x)

    
if __name__ == '__main__':
    main()
