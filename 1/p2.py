def main():
    target = 2020
    lookup = {}
    # Load all numbers
    with open('input.txt', 'r') as f:
        for line in f:
            num = int(line)
            lookup[num] = target - num

    for k1, v in lookup.items():
        for k2 in lookup:
            if k1 == k2:
                continue
            k3 = v - k2
            if k3 in lookup:
                print(f'Goal = {k1 * k2 * k3}')
                return
    print('Failure!')

if __name__ == '__main__':
    main()
