from utils import *
import re
import copy
from functools import *
from collections import *
import math

LIST = []

# circular linked list with indexing woo!!!!
class ListNode:
    def __init__(self, label, nextnode):
        self.label = label
        self.next = nextnode

    def get_label(self):
        return self.label

    def set_next(self, nextnode):
        self.next = nextnode

    def get_next(self):
        return self.next

def main():
    global LIST
    # Load all lines
    inp = '487912365'
    #inp = '389125467'
    cups = list(inp)
    for i in range(1000000):
        LIST.append(ListNode(i+1, None))
    
    # Link start and end
    first = LIST[int(cups[0])-1]
    last = LIST[len(LIST)-1]
    last.set_next(first)
    
    # Link starting cups
    for i in range(1,len(cups)):
        prevnode = LIST[int(cups[i-1])-1]
        node = LIST[int(cups[i])-1]
        prevnode.set_next(node)
    
    # Link starting to rest
    lastcup = LIST[int(cups[len(cups)-1])-1]
    nextcup = LIST[len(cups)]
    lastcup.set_next(nextcup)

    # Link remaining cups
    for i in range(len(cups)+1, len(LIST)):
        prevnode = LIST[i-1]
        nextnode = LIST[i]
        prevnode.set_next(nextnode)

    currcup = first
    for k in range(10000000):
        if k % 1000000 == 0:
            p(k)
        cuplen = len(cups)
        #print(f'curr = {currcup.get_label()}')
        chosen = []
        nextcup = currcup.get_next()
        for _ in range(3):
            chosen.append(nextcup)
            nextcup = nextcup.get_next()
        #print(f'pick up = {[c.get_label() for c in chosen]}')
        currcup.set_next(nextcup) # broken?
        nextlabel = currcup.get_label() - 1
        if nextlabel == 0:
            nextlabel = len(LIST)
        chosen_labels = [c.get_label() for c in chosen]
        while nextlabel in chosen_labels:
            nextlabel -= 1
            if nextlabel == 0:
                nextlabel = len(LIST)
        #print(f'destination = {nextlabel}')
        insert_at_cup = LIST[nextlabel-1]
        end_insert = insert_at_cup.get_next()
        insert_at_cup.set_next(chosen[0])
        chosen[len(chosen)-1].set_next(end_insert)
        currcup = currcup.get_next()
    cup1 = LIST[0].get_next()
    cup2 = cup1.get_next()
    result = cup1.get_label() * cup2.get_label()
    p(result)

if __name__ == '__main__':
    main()
