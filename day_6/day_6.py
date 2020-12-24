
def count_anyone_answered_yes(groups):
    sum = 0
    for group in groups:
        c = set(group)
        c.discard('\n')
        sum += len(c)
    return sum

def count_everyone_answered_yes(groups):
    sum = 0
    for group in groups:
        people = (set(person) for person in group.split('\n'))
        common_answers = set.intersection(*people)
        sum += len(common_answers)
    return sum

if __name__ == "__main__":
    with open("day_6/input.txt") as fin:
        groups = fin.read().split("\n\n")
        print(count_anyone_answered_yes(groups))
        print(count_everyone_answered_yes(groups))