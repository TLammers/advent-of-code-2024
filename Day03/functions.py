def read_file_lines(file_name):
    """Reads a file line by line and returns a list containing the string read from each line"""
    file_input = open(file_name, 'r')
    list = file_input.readlines()
    file_input.close()
    return list