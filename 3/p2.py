
def main():
    # Load all lines
    lines = []
    paths = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    max_right = len(lines[0])
    max_down = len(lines)

    value = 1
    for path in paths:
        right = path[0]
        down = path[1]
        pos = [0, 0]
        ntrees = 0
        pos[0] += down
        while pos[0] < max_down:
            pos[1] += right
            pos[1] %= max_right
            ntrees += (lines[pos[0]][pos[1]] == '#')
            pos[0] += down
        value *= ntrees


    print(f'VALUE = {value}')

if __name__ == '__main__':
    main()
