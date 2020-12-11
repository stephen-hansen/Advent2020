from utils import *
import re
import copy


def apply_rules(rows):
    new_rows = copy.deepcopy(rows)
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            curr = rows[i][j]
            adj = []
            c = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if k == i and l == j:
                        continue
                    if k >= 0 and k < len(rows) and l >= 0 and l < len(rows[k]):
                        adj.append(rows[k][l])
            if curr == 'L' and all(list(map(lambda x: x != '#', adj))):
                new_rows[i][j] = '#'
            elif curr == '#' and sum(list(map(lambda x: x == '#', adj))) >= 4:
                new_rows[i][j] = 'L'
    return new_rows

def main():
    # Load all lines
    lines = getlines()
    lines = list(map(list, lines))
    while True:
        old_lines = lines
        print(lines)
        lines = apply_rules(old_lines)
        if old_lines == lines:
            break
    p(sum(map(lambda x: x.count('#'), lines)))


if __name__ == '__main__':
    main()
