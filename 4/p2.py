import re

def main():
    # Load all lines
    lines = []
    with open('input.txt', 'r') as f:
        lines = f.read()
        lines = lines.split('\n\n')
    lines = [x.replace('\n', ' ') for x in lines]
    answer = 0
    for line in lines:
        valid = True
        needed = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
        for keyval in line.split(' '):
            data = keyval.split(':')
            if len(data) != 2:
                continue
            key = data[0]
            val = data[1]
            needed.remove(key)
            if valid:
                if key == 'byr':
                    nval = int(val)
                    valid = nval >= 1920 and nval <= 2002
                elif key == 'iyr':
                    nval = int(val)
                    valid = nval >= 2010 and nval <= 2020
                elif key == 'eyr':
                    nval = int(val)
                    valid = nval >= 2020 and nval <= 2030
                elif key == 'hgt':
                    if not bool(re.match('^\d+(cm|in)$', val)):
                        valid = False
                    elif val[-2:] == 'cm':
                        val = int(val[:-2])
                        valid = val >= 150 and val <= 193
                    elif val[-2:] == 'in':
                        val = int(val[:-2])
                        valid = val >= 59 and val <= 76
                    else:
                        valid = False
                elif key == 'hcl':
                    valid = (bool(re.match(r'^#([a-f]|\d){6}$', val)))
                elif key == 'ecl':
                    valid = bool(re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', val))
                elif key == 'pid':
                    valid = bool(re.match(r'^(\d){9}$', val))
                elif key == 'cid':
                    valid = True
        if valid and (len(needed) == 0 or (len(needed) == 1 and needed[0] == 'cid')):
            answer += 1

    print(answer)

if __name__ == '__main__':
    main()
