import re
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

# https://rosettacode.org/wiki/Chinese_remainder_theorem
# n, a lists of ints, same length
# n the list of modulo bases
# a the list of remainders (modulo congruences)
# ex: x = 2 (mod 3) = 3 (mod 5) = 2 (mod 7)
# n = [3, 5, 7]
# a = [2, 3, 2]
# answer is 23 (23 % 3 = 2, 23 % 5 = 3, 23 % 7 = 2)
def crt(n, a):
    N = reduce(lambda x, y: x*y, n)
    x = 0
    for i in range(len(n)):
        ni = n[i]
        ai = a[i]
        pi = N//ni
        si = mul_inv(pi, ni)
        x += ai * si * pi
    x = x % N
    return x

def p(arg):
    print(arg)

def getinput():
    with open('input.txt', 'r') as f:
        return f.read()

def getdbnldata():
    data = utils.getinput()
    groups = data.split('\n\n')
    for i in range(len(groups)):
        groups[i] = list(filter(lambda x: x != '', groups[i].split('\n')))
    return groups

def getlines():
    return getinput().splitlines()

def getlines_map(func):
    return list(map(func, getlines()))

def getlines_int():
    return getlines_map(int)

def getlines_strip():
    return getlines_map(lambda x: x.strip())

def getlines_getsv(delim=','):
    return getlines_map(lambda x: x.split(delim))

def getlines_getsv_int(delim=','):
    return list(map(lambda x: list(map(int, x)), getlines_getsv(delim)))

def getlines_map_regex(pattern_string):
    return getlines_map(lambda x: re.fullmatch(re.compile(pattern_string), x))

def getlines_filter(func):
    lines = getlines()
    return list(filter(func, lines))

def getlines_filter_regex(pattern_string):
    return getlines_filter(lambda x: bool(re.fullmatch(re.compile(pattern_string), x)))

class Node:
    def __init__(self, children=[], directed=False, label=None):
        self.children = children
        self.directed = directed
        self.label = None

    def add_child(self, child):
        self.children.append(child)
        if not self.directed:
            child.add_child_back(self)

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def add_child_back(self, child):
        self.children.append(child)

    def set_parent(self, parent):
        self.parent = parent

    def bfs(self, target):
        discovered = {self}
        queue = [[self]]
        while len(Q) != 0:
            path = queue.pop(0)
            v = path[-1]
            if v == target:
                return path
            for child in self.children:
                if child not in discovered:
                    discovered.add(child)
                    queue.append(list(path).append(child))

class Graph:
    def __init__(self, graph={}, directed=False):
        self.graph = graph
        self.directed = directed

    def get_node(self, name):
        return self.graph[name]

    def get_nodes(self, filt=None):
        nodes = list(self.graph.values())
        if filt:
            nodes = filter(filt, nodes)
        return nodes

    def add_node(self, name, cnames=[], label=None):
        self.graph[name] = Node(name)
        for c in cnames:
            if c not in self.graph:
                self.graph[c] = Node(c, self.directed, label)
            self.graph[name].add_child(self.graph[c])
        self.graph[name] = Node(name, children)
        return self.graph[name]

    def bfs(self, sourcename, targetname):
        source = self.graph[sourcename]
        target = self.graph[targetname]
        return source.bfs(target)

