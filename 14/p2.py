from utils import *
import re
import copy
from functools import *

def mask(v, mask):
    mask_v = int(mask.replace('0', 'Q').replace('1', '0').replace('X','0').replace('Q', '1'), 2)
    keep = mask_v & v
    mask_o = int(mask.replace('X', '0'), 2)
    over = mask_o | keep
    values = []
    masks = []
    combos = mask.count('X')
    for i in range(2**combos):
        n = '{0:b}'.format(i).zfill(combos)
        new_m = copy.deepcopy(list(mask))
        q = 0
        for j in range(len(new_m)):
            if new_m[j] == 'X':
                new_m[j] = n[q]
                q += 1
            else:
                new_m[j] = '0'
        masks.append(int(''.join(new_m), 2))
    for m in masks:
        values.append(over + m)

    return values

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
            ks = mask(k, bitmask)
            for k in ks:
                mem[k] = v
    s = 0
    for v in mem.values():
        s += v
    print(s)

        
if __name__ == '__main__':
    main()
