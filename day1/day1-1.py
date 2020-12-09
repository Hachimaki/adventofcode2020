def main():
    values = setup_input("day1-1input.txt")
    print(values)
    a, b = search(values)
    print(a)
    print(b)
    print("result: ", result(a, b))


def setup_input(input_file):
    values = {}

    with open(input_file) as input_values:
        for line in input_values:
            # map values by string/int of the value
            values[line.rstrip()] = int(line)

    return values


# receive a dict of string/int values to compare
# need to find which pair sums to 2020
def search(values):
    keys = values.keys()

    for key in keys:
        test_val = 2020 - int(values[key])
        if str(test_val) in values:
            return values[key], test_val

    return -1, -1


def result(a, b):
    return a * b


if __name__ == "__main__":
    main()
