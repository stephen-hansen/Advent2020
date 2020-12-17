import utils
from math import floor, ceil

def main():
    # Load all lines
    data = utils.getinput()
    groups = data.split('\n\n')
    answer = 0
    for group in groups:
        yes = {}
        persons = list(filter(lambda x: x != '', group.split('\n')))
        for person in persons:
            for c in person:
                if c not in yes:
                    yes[c] = 1
                else:
                    yes[c] += 1
        for k, v in yes.items():
            if v == len(persons):
                answer += 1
    print(answer)

if __name__ == '__main__':
    main()
