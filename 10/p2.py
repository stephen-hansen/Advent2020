import utils
import re
import copy

precomputed = {}

def get_arrangements(curr_jolt, jolts):
    global precomputed
    if curr_jolt in precomputed:
        return precomputed[curr_jolt]
    if curr_jolt == max(jolts):
        precomputed[curr_jolt] = 1
        return 1
    next_jolt = [curr_jolt+1, curr_jolt+2, curr_jolt+3]
    total = 0
    for j in next_jolt:
        if j in jolts:
            total += get_arrangements(j, jolts)
    precomputed[curr_jolt] = total
    return total

def main():
    # Load all lines
    lines = sorted(utils.getlines_int())
    max_jolt = max(lines) + 3
    lines.append(max_jolt)
    print(get_arrangements(0, lines)) 

if __name__ == '__main__':
    main()
