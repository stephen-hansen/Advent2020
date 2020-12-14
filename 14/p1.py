from utils import *
import re
import copy
from functools import *

def mask(v, mask):
    mask_v = int(mask.replace('1', '0').replace('X', '1'), 2)
    mask_n = int(mask.replace('X', '0'), 2)
    return (mask_v & v) + mask_n

def main():
    # Load all lines
    lines = getlines_map(lambda x: x.split(' = '))
    mem = {}
    bitmask = None
    for l in lines:
        t = l[0]
        v = l[1]
        if t == 'mask':
            bitmask = v
        else:
            m = re.fullmatch(re.compile(r'mem\[(\d+)\]'), t)
            k = int(m.group(1))
            v = int(v)
            mem[k] = mask(v, bitmask)
    s = 0
    for v in mem.values():
        s += v
    print(s)

        
if __name__ == '__main__':
    main()
