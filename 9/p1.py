import utils
import re


def main():
    # Load all lines
    lines = list(utils.getlines_int())
    preamble = lines[:25]
    for i in range(25, len(lines)):
        valid = set([x + y for x in preamble for y in preamble if x != y])
        print(preamble)
        if lines[i] not in valid:
            print(lines[i])
            break
        preamble = lines[i-24:i+1]


if __name__ == '__main__':
    main()
