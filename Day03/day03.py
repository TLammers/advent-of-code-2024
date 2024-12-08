from functions import *
import re

# file_name = 'test.txt'
file_name = 'input.txt'

def parse_mult_statements(line):
    """
    Parses all instances of 'mul(#,#)' from a string and returns a list of the instances.
    """
    result = []

def parse_multiply_statement(str):
    """
    Takes a group of (<full string>, <first number>, <second number>) and ret
    """

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
            print('result: ' + str(result) + ' // multiplied_result: ' + str(multiplied_result))
    
    print('part 1 result: ' + str(result))
            


part_one()
