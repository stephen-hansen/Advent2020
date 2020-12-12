from utils import *
import re
import copy

def rotate_left(d):
    new_d = []
    m = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    for i in d:
        new_d.append(m[i])
    return new_d

def rotate_right(d):
    new_d = []
    m = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    for i in d:
        new_d.append(m[i])
    return new_d

def main():
    # Load all lines
    lines = getlines()
    d = 'E'
    spos = [0, 0]
    pos = spos
    w = [1, 10]
    d = ['N', 'E']
    #lines = ['F10', 'N3', 'F7', 'R90', 'F11']
    for l in lines:
        path = l[0]
        n = int(l[1:])
        p(l)
        if path == 'N':
            w[0] += n
        elif path == 'S':
            w[0] -= n
        elif path == 'E':
            w[1] += n
        elif path == 'W':
            w[1] -= n
        elif path == 'L':
            o_d = copy.deepcopy(d)
            for x in range(n//90):
                new_w = [w[1], -w[0]]
                w = new_w
        elif path == 'R':
            o_d = copy.deepcopy(d)
            for x in range(n//90):
                new_w = [-w[1], w[0]]
                w = new_w
        elif path == 'F':
            pos[0] += w[0] * n
            pos[1] += w[1] * n
        p(w)
        p(pos)
    print(abs(pos[0]) + abs(pos[1]))

if __name__ == '__main__':
    main()
