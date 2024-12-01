from collections import Counter

def main():
    list1, list2 = get_lists_from_input()
    print(f'Total distance is: {get_distance(list1, list2)}')
    print(f'Total similarity is: {get_similarity(list1, list2)}')
    return

def get_lists_from_input():
    list1, list2 = [], []

    for line in open('day1_input.txt', 'r'):
        space_idx = line.find(' ')
        list1.append(int(line[:space_idx]))
        list2.append(int(line[space_idx + 1:]))

    return [list1, list2]

# Part 1
def get_distance(list1, list2):
    return sum(abs(location1 - location2) for location1, location2 in zip(sorted(list1), sorted(list2)))

# Part 2
def get_similarity(list1, list2):
    count2 = Counter(list2)
    return sum(key * value * count2[key] for key, value in Counter(list1).items())

if __name__ == '__main__':
    main()
