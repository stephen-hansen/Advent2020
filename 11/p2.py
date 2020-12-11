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
            dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
            for d in dirs:
                x = i
                y = j
                while True:
                    x += d[0]
                    y += d[1]
                    if x >= 0 and x < len(rows) and y >= 0 and y < len(rows[x]):
                        if rows[x][y] != '.':
                            adj.append(rows[x][y])
                            break
                    else:
                        break
            if curr == 'L' and all(list(map(lambda x: x != '#', adj))):
                new_rows[i][j] = '#'
            elif curr == '#' and sum(list(map(lambda x: x == '#', adj))) >= 5:
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
