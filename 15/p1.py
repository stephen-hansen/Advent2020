from utils import *
import re
import copy
from functools import *
from collections import *

def main():
    # Load all lines
    vs = '11,0,1,10,5,19'.split(',')
    last = int(vs[len(vs)-1])
    spoken = defaultdict(list)
    for i in range(len(vs)):
        spoken[int(vs[i])].append(i+1)
    i = len(vs)+1
    while i <= 2020:
        if len(spoken[last]) == 1:
            last = 0
            spoken[last].append(i)
        else:
            l = spoken[last]
            last = l[len(l)-1] - l[len(l)-2]
            spoken[last].append(i)
        i+=1
    print(last)


    
        
if __name__ == '__main__':
    main()
