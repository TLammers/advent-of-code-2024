

# file_name = './test.txt'
file_name = 'input.txt'




def read_file_lines(file_name):
    """Reads a file line by line and returns a list containing the string read from each line"""
    file_input = open(file_name, 'r')
    list = file_input.readlines()
    file_input.close()
    return list

fn_comparison_asc = lambda int: int > 3
fn_comparison_desc = lambda int: int > -3

def part_one():
    """Solution for part 1"""
    input_arrays = [x.split() for x in read_file_lines(file_name)]
    valid_count = 0
    # print([int(x) for x in input_arrays[0]])
    # print(part_one_loop_check([int(x) for x in input_arrays[0]]))
    for x in input_arrays:
        
        if(sorted(x) == x):
            print('asc: ' + str(x))
            # row is ascending
            # For each number in the row
            for i in range(0, len(x)-1):
                num_one = int(x[i])
                num_two = int(x[i+1])
                num_two_comp = num_one + 3
                if (num_two_comp > num_two):
                    print(str(num_one) + ',' + str(num_two) + ': pass')
                else:
                    print(str(num_one) + ',' + str(num_two) + ': fail')

                # if(num_one + 3 >= num_two & num_one - num_two > 0):
                #     print('pass: [' + str(num_one) + ',' + str(num_two) + ']')
                #     continue
                #     # pass
                # else:
                #     print('INVALID: [' + str(num_one) + ',' + str(num_two) + ']' )
                #     break;
            else:
                valid_count = valid_count + 1

        elif(sorted(x, reverse=True) == x):
            print('desc: ' + str(x))
            # row is descending
            for i in range(0, len(x)-1):
                num_one = int(x[i])
                num_two = int(x[i+1])
                num_two_comp = num_one - 3
                if (num_two_comp > num_two):
                    print(str(num_one) + ',' + str(num_two) + ': pass')
                else:
                    print(str(num_one) + ',' + str(num_two) + ': fail')
                # if(num_one - 3 <= num_two & num_two - num_one > 0):
                #     print('pass: [' + str(num_one) + ',' + str(num_two) + ']')
                #     continue
                #     # pass
                # else:
                #     print('INVALID: [' + str(num_one) + ',' + str(num_two) + ']' )
                #     break;
            else:
                valid_count = valid_count + 1
    print('valid count: ' + str(valid_count))
    # print(input_split)


def part_one_loop_check(list, fn_comparison):
    for x in range(0, len(list)-1):
        if((list[x] != list[x+1]) & (fn_comparison(int(list[x]) + 3 > int(list[x+1])))):
            print(str(list) + ': unsafe')
            return False
    else:
        return True




def part_two():
    """Solution for part 2"""
    # TODO

def main():
    part_one()
    part_two()

main()