from utils import *
import re
import copy

def main():
    # Load all lines
    lines = getlines()
    e_t = int(lines[0])
    best_id = None
    best_diff = float("inf")
    s = lines[1].split(',')
    for i in s:
        if i == 'x':
            continue
        t = 0
        p(i)
        while t < e_t:
            t += int(i)
        p(t)
        diff = t - e_t
        if diff < best_diff:
            best_diff = diff
            best_id = i
    p(int(best_id) * int(best_diff))
    
if __name__ == '__main__':
    main()
