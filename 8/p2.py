import utils
import re
import copy

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
    for i in range(len(instrs)):
        print(i)
        instrs_copy = copy.deepcopy(instrs)
        change = instrs_copy[i][0]
        if change == 'acc':
            continue
        elif change == 'jmp':
            instrs_copy[i][0] = 'nop'
        else:
            instrs_copy[i][0] = 'jmp'
        valid = False
        pc = 0
        acc = 0
        while True:
            if pc >= len(instrs_copy):
                valid = True
                break
            instr = instrs_copy[pc]
            name = instr[0]
            amt = instr[1]
            instrs_copy[pc][2] += 1
            if instrs_copy[pc][2] == 2:
                break
            if name == 'acc':
                acc += amt
                pc += 1
            elif name == 'jmp':
                pc += amt
            elif name == 'nop':
                pc += 1
        if valid:
            print(acc)
            break

if __name__ == '__main__':
    main()
