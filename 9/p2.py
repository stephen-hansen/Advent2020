import utils
import re


def main():
    # Load all lines
    lines = list(utils.getlines_int())
    inv = 10884537
    for i in range(len(lines)):
        for j in range(len(lines)):
            if sum(lines[i:j]) == inv:
                print(min(lines[i:j]) + max(lines[i:j]))


if __name__ == '__main__':
    main()
