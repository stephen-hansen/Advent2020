import utils
from math import floor, ceil

def main():
    # Load all lines
    data = utils.getinput()
    groups = data.split('\n\n')
    answer = 0
    for group in groups:
        yes = set()
        for person in group.split('\n'):
            for c in person:
                yes.add(c)
        answer += len(yes)
    print(answer)

if __name__ == '__main__':
    main()
