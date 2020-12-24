
def find_two_entries_which_sum_to_2020(entry_set):
    for first_num in entry_set:
        possible_second_num = 2020 - first_num
        if possible_second_num in entry_set:
            return (first_num, possible_second_num)
    return (0,0)

def find_three_entries_which_sum_to_2020(entry_set):
    for first_num in entry_set:
        for second_num in entry_set:
            possible_third_num = 2020 - first_num - second_num
            if possible_third_num in entry_set:
                return (first_num, second_num, possible_third_num)
    return (0,0,0)

if __name__ == "__main__":
    with open("day_1/input.txt") as input_file:
        entry_list = input_file.readlines()
        entry_set = set(map(lambda num_str: int(num_str), entry_list))

        two_entries = find_two_entries_which_sum_to_2020(entry_set)
        print(two_entries[0] * two_entries[1])

        three_entries = find_three_entries_which_sum_to_2020(entry_set)
        print(three_entries[0] * three_entries[1] * three_entries[2])


