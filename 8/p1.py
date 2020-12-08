import utils
import re


def main():
    # Load all lines
    lines = utils.getlines_map_regex(r'(\S\S\S) ([+-]\d+)')
    answer = 0
    instrs = []
    acc = 0
    for l in lines:
        instr = l.groups(1)[0]
        number = int(l.groups(1)[1])
        instrs.append([instr, number, 0])
    pc = 0
    while True:
        instr = instrs[pc]
        name = instr[0]
        amt = instr[1]
        instrs[pc][2] += 1
        if instrs[pc][2] == 2:
            break
        if name == 'acc':
            acc += amt
            pc += 1
        elif name == 'jmp':
            pc += amt
        elif name == 'nop':
            pc += 1
    print(acc)

if __name__ == '__main__':
    main()
