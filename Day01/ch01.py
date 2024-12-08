from functions import *

# file_name = 'test.txt'
file_name = 'input.txt'
file_input_name = '/mnt/c/Users/tyson/documents/development/advent-of-code-2024/aoc2024/ch01/' + file_name

def part_one():
    """Solution definition for part 1"""

    list_one = []
    list_two = []
    list_distances = []

    list = read_file_lines(file_input_name)


    # split the input into the two vertical lists
    for x in list:
        split = x.split('   ')
        list_one.append(int(split[0]))
        list_two.append(int(split[1]))

    # sort the lists in place
    list_one.sort()
    list_two.sort()

    for x in range(len(list_one)):
        list_distances.append(abs(list_one[x] - list_two[x]))
    
    print('solution part 1: ' + str(sum(list_distances)))

def part_two():
    """Solution definition for part 2"""
    list_one = []
    list_two = []
    list_distances = []

    list = read_file_lines(file_input_name)


    # split the input into the two vertical lists
    for x in list:
        split = x.split('   ')
        list_one.append(int(split[0]))
        list_two.append(int(split[1]))

    # Create a dict of <number, occurence_count> for each number in the left list
    # to its count in the right
    dict_counts = [x * list_two.count(x) for x in list_one]
    # for x in dict_counts:
    #     print(x)
    print('solution part 2: ' + str(sum(dict_counts)))
    # for x in list_one:




part_one()
part_two()