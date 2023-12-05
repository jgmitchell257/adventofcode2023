# aoc_utils.py

def load_input(x):
    input_file = open(x,"r")
    input_data = input_file.readlines()
    output_data = []
    for line in input_data:
        line = line.strip("\n")
        output_data.append(line)
    return output_data