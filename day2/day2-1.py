def main():
    passwords = setup_input("day2input.txt")
    count = 0
    for password in passwords:
        if is_valid_password(password):
            count += 1
    print("valid passwords: ", count)


def setup_input(input_file):
    passwords = []

    with open(input_file) as input_values:
        for line in input_values:
            password = []

            # TODO: redo as a regular expression to be smrat
            # password format: low-high target_char: password
            hyphen_split = line.rstrip().split("-")
            # here is [low, high target_char: password]
            password.append(hyphen_split[0])
            space_split = hyphen_split[1].split(" ")
            # here is [high, target_char:, password]
            password.append(space_split[0])
            password.append(space_split[1].strip(":"))
            password.append(space_split[2])

            passwords.append(password)

    return passwords


# check if a password is valid based on the password policy
# password policy: low-high target_char: password
# password is valid if it contains between low and high counts of target_char
def is_valid_password(password_set):
    low = int(password_set[0])
    high = int(password_set[1])
    target_char = password_set[2]
    password = password_set[3]

    letters = {}

    for char in password:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    if target_char in letters and low <= letters[target_char] <= high:
        return True

    return False


if __name__ == "__main__":
    main()
