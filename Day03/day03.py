from functions import *
import re

# file_name = 'test.txt'
file_name = 'input.txt'

def part_one():
    """Solution definition for part 1"""
    list = read_file_lines(file_name)
    result = 0
    for line in list:
        print(line)
        group = re.findall('(mul\((\d{1,3})\,(\d{1,3})\))', line)
        for (fullStr, numOne, numTwo) in group:
            multiplied_result = int(numOne) * int(numTwo)
            result += multiplied_result
    
    print('part 1 result: ' + str(result))

def part_two():
    list = read_file_lines(file_name)
    part_two_result = 0
    last_do_dont_was_do = True
    for k in range(0, len(list)):
        line = list[k]
        # find all instances of 'do()', 'dont()', or the regex of part 1
        group = re.findall('((don\'t\(\))|(do\(\))|(mul\((\d{1,3})\,(\d{1,3})\)))', line)
        line_result = 0
        for i in range(0, len(group)):
            (string, _, _, stmt, numOne, numTwo) = group[i]
            if (string.startswith('do()')):
                last_do_dont_was_do = True
                continue
            elif (string.startswith('don\'t()')):
                # print('dont')
                last_do_dont_was_do = False
                continue
            elif (string.startswith('mul')):
                if (last_do_dont_was_do == True):
                    # print('last do was do - adding')
                    multiplied_result = int(numOne) * int(numTwo)
                    line_result += multiplied_result
                elif (last_do_dont_was_do == False):
                    # print('last do was dont - not adding')
                    continue
        part_two_result += line_result
        
    print('part 2 result: ' + str(part_two_result))

    


part_one()
part_two()