
from collections import Counter

def parse_line(line):
    parts = line.split(" ")
    min, max = map(lambda n: int(n), parts[0].split("-"))
    letter = parts[1][0]
    password = parts[2]
    return (min, max, letter, password)

def validate_passwords_with_old_policy(lines):
    valid_password_count = 0
    for line in lines:
        min, max, letter, password = parse_line(line)
        count_of = Counter(password)
        if count_of[letter] >= min and count_of[letter] <= max:
            valid_password_count += 1
    return valid_password_count

def validate_passwords_with_current_policy(lines):
    valid_password_count = 0
    for line in lines:
        firs_pos, second_pos, letter, password = parse_line(line)
        if (password[firs_pos - 1] == letter) ^ (password[second_pos - 1] == letter):
            valid_password_count += 1
    return valid_password_count

if __name__ == "__main__":
    valid_password_count = 0
    with open("day_2/input.txt") as input_file:
        lines = input_file.readlines()

        valid_password_count_old = validate_passwords_with_old_policy(lines)
        print(valid_password_count_old)

        valid_password_count_current = validate_passwords_with_current_policy(lines)
        print(valid_password_count_current)

