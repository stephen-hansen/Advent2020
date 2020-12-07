import utils
import re

def contains(target, source, lookup):
    if target in lookup[source]:
        return True
    else:
        for k in lookup[source]:
            if contains(target, k, lookup):
                return True
        return False

def main():
    # Load all lines
    lines = utils.getlines()
    answer = 0
    containpattern = r'((\d+) (\w+ \w+) bags?[.,]\s?)+?'
    sourcepattern = re.compile(r'(\w+ \w+) bags? contain')
    rules = {}
    for l in lines:
        source = re.match(sourcepattern, l)
        name = source.groups(1)[0]
        rules[name] = {}
        for m in re.finditer(containpattern, l):
            rules[name][m.groups(2)[2]] = int(m.groups(1)[1])
    target = 'shiny gold'
    print(rules)
    for rule in rules:
        if rule == target:
            continue
        answer += int(contains(target, rule, rules))
    print(answer)

if __name__ == '__main__':
    main()
