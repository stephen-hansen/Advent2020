
def main():
    # Load all lines
    lines = []
    with open('input.txt', 'r') as f:
        lines = f.read()
        lines = lines.split('\n\n')
    lines = [x.replace('\n', ' ') for x in lines]
    answer = 0
    for line in lines:
        print(line)
        needed = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
        for keyval in line.split(' '):
            data = keyval.split(':')
            if len(data) != 2:
                continue
            key = data[0]
            val = data[1]
            needed.remove(key)
        if len(needed) == 0 or (len(needed) == 1 and needed[0] == 'cid'):
            answer += 1

    print(answer)

if __name__ == '__main__':
    main()
