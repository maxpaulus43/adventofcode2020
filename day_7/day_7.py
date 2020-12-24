from collections import defaultdict
from typing import Deque

def parse_line(line):
    lhs, rhs = line[:-2].split(' contain ')
    parent_bag = lhs[:-4].strip()
    child_bag_strs = (s.strip() for s in rhs.split(','))

    children_bags = []

    for child_bag_str in child_bag_strs:
        count = child_bag_str[:1]
        if child_bag_str[-1] == 's':
            child_bag = child_bag_str[1:-4]
        else:
            child_bag = child_bag_str[1:-3]
        child_bag = child_bag.strip()

        children_bags.append((child_bag, count))

    return children_bags, parent_bag

def count_bags_which_can_hold_bag(bag_of_interest, what_contains):
    bag_count = 0
    visited = set()
    qualified_bags = Deque(what_contains[bag_of_interest])

    while len(qualified_bags) > 0:
        parent_bag = qualified_bags.popleft()
        if parent_bag not in visited:
            bag_count += 1
            for b in what_contains[parent_bag]:
                qualified_bags.append(b)
            visited.add(parent_bag)

    return bag_count

def count_total_bags_contained_within_bag(bag_of_interest, whats_in):
    bag_count = 0

    qualified_bags = Deque(whats_in[bag_of_interest])
    while len(qualified_bags) > 0:
        child_bag = qualified_bags.popleft()

        number_of_bags = child_bag[1]
        if number_of_bags == 'n':
            continue
        number_of_bags = int(number_of_bags)

        bag_count += number_of_bags
        for _ in range(number_of_bags):
            for b in whats_in[child_bag[0]]:
                qualified_bags.append(b)

    return bag_count

if __name__ == "__main__":
    # key=bag, value=set of bags which directly contain the key bag
    what_contains = defaultdict(set)
    # key=bag, value=list of bags directly contained within the key bag
    whats_in = defaultdict(list)

    with open("day_7/input.txt") as fin:
        for line in fin:
            child_bags, parent_bag = parse_line(line)
            whats_in[parent_bag] = child_bags
            for child_bag, _ in child_bags:
                what_contains[child_bag].add(parent_bag)

    print(count_bags_which_can_hold_bag('shiny gold', what_contains))
    print(count_total_bags_contained_within_bag('shiny gold', whats_in))          
