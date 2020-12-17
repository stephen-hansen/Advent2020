import re

def main():
    p = re.compile(r'(\d+)-(\d+)\s([a-z]):\s([a-z]+)')
    # Load all lines
    nvalid = 0
    with open('input.txt', 'r') as f:
        for line in f:
            m = p.match(line)
            p1, p2, l, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
            nvalid += ((password[p1-1] == l) != (password[p2-1] == l))

    print(f'NUM VALID = {nvalid}')

if __name__ == '__main__':
    main()
