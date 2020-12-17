def main():
    target = 2020
    lookup = {}
    # Load all numbers
    with open('input.txt', 'r') as f:
        for line in f:
            num = int(line)
            lookup[num] = target - num

    for k, v in lookup.items():
        if v in lookup:
            print(f'Goal = {k * v}')
            return
    print('Failure!')

if __name__ == '__main__':
    main()
