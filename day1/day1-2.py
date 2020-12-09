def main():
    values = setup_input("day1-1input.txt")
    a, b, c = search(values)
    print(a)
    print(b)
    print(c)
    print("result: ", result(a, b, c))


def setup_input(input_file):
    values = {}

    with open(input_file) as input_values:
        for line in input_values:
            # map values by string/int of the value
            values[line.rstrip()] = int(line)

    return values


# receive a dict of string/int values to compare
# need to find which triple sums to 2020
def search(values):
    keys = list(values.keys())

    for i in range(len(keys)):
        for j in range(len(keys)):
            if j == i:
                continue
            else:
                test_val = 2020 - int(values[keys[i]]) - int(values[keys[j]])
                if str(test_val) in values:
                    return int(values[keys[i]]), int(values[keys[j]]), test_val

    return -1, -1, -1


def result(a, b, c):
    return a * b * c


if __name__ == "__main__":
    main()
