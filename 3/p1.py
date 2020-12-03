
def main():
    # Load all lines
    lines = []
    right = 3
    down = 1
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    max_right = len(lines[0])
    max_down = len(lines)
    pos = [0, 0]
    ntrees = 0
    pos[0] += down
    while pos[0] < max_down:
        pos[1] += right
        pos[1] %= max_right
        ntrees += (lines[pos[0]][pos[1]] == '#')
        pos[0] += down


    print(f'NUM TREES = {ntrees}')

if __name__ == '__main__':
    main()
