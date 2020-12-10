import utils
import re


def main():
    # Load all lines
    lines = sorted(utils.getlines_int())
    max_jolt = max(lines) + 3
    lines.append(max_jolt)
    curr_jolt = 0
    differences = {}
    chain = []
    while True:
        allowed_jolts = [curr_jolt+1, curr_jolt+2, curr_jolt+3]
        all_fail = True
        for j in allowed_jolts:
            if j in lines:
                chain.append(j)
                diff = j - curr_jolt
                curr_jolt = j
                if diff not in differences:
                    differences[diff] = 0
                differences[diff] += 1
                all_fail = False
                break
        if all_fail:
            break
    print(differences[1])
    print(differences[3])
    print(differences[1] * differences[3])
    

if __name__ == '__main__':
    main()
