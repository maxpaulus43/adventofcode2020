
def find_possible_sums_from_nums(nums):
    sums = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sums.add(nums[i] + nums[j])
    return sums

def find_weak_number(preamble_len, input):
    for i in range(preamble_len, len(input)):
        num = input[i]
        sums = find_possible_sums_from_nums(input[i - preamble_len:i])
        if num not in sums:
            return num

def find_encryption_weakness(weak_number, nums):
    prefix_sums = list(nums)
    prefix_sums.insert(0, 0)
    for i in range(1, len(nums)):
        prefix_sums[i] += prefix_sums[i - 1]

    for i in range(len(nums)):
        for j in range(i + 2, len(nums)):
            if prefix_sums[j] - prefix_sums[i] == weak_number:
                return nums[i:j]

if __name__ == "__main__":
    with open("day_9/input.txt") as fin:
        input = list(map(int, fin))

    # part 1
    weak_number = find_weak_number(25, input)
    print(weak_number)

    #part 2
    encryption_weakness = find_encryption_weakness(weak_number, input)
    print(min(encryption_weakness) + max(encryption_weakness))
