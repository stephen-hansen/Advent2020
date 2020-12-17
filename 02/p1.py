import re

def main():
    p = re.compile(r'(\d+)-(\d+)\s([a-z]):\s([a-z]+)')
    # Load all lines
    nvalid = 0
    with open('input.txt', 'r') as f:
        for line in f:
            m = p.match(line)
            lmin, lmax, l, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
            nvalid += (lmin <= password.count(l) <= lmax)

    print(f'NUM VALID = {nvalid}')

if __name__ == '__main__':
    main()
