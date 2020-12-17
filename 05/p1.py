import utils
from math import floor, ceil

def main():
    # Load all lines
    lines = utils.getlines()
    #lines = ['FBFBBFFRLR', 'BFFFBBFRRR']
    answer = 0
    for line in lines:
        print(line)
        mini = 0
        maxi = 127
        for c in line[:7]:
            size = maxi-mini
            if c == 'F':
                maxi = maxi - size/2
            elif c == 'B':
                mini = mini + size/2
        mini2 = 0
        maxi2 = 7
        for c in line[7:]:
            size = maxi2-mini2
            if c == 'L':
                maxi2 = maxi2 - size/2
            elif c == 'R':
                mini2 = mini2 + size/2
        seat = (ceil(mini), floor(maxi2))
        print(seat)
        id = seat[0] * 8 + seat[1]
        answer = id if id > answer else answer

    print(answer)

if __name__ == '__main__':
    main()
