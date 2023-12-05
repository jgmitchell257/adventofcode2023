# Advent of Code - Day 3
import re
import aoc_utils

# import data
original_data = aoc_utils.load_input("day03/sample")


# build matrix from data
def build_matrix(data):
    matrix = []

    for row in data:
        # get rid of newline characters
        row = row.strip("\n")

        holder = []
        for character in row:
            holder.append(character)
        matrix.append(holder)

    return matrix


matrix = build_matrix(original_data)


# find special characters and create a set
def get_char_set(matrix_data):
    char_set = []
    for row in matrix_data:
        for character in row:
            if not re.match(r"\d|\.", character):
                char_set.append(character)

    return list(set(char_set))


char_set = get_char_set(matrix)


# scan matrix for special character
def get_char_locations(matrix, char_set):
    char_loc = []
    row_num = 0
    for row in matrix:
        for idx, column in enumerate(row):
            for i in char_set:
                if column == i:
                    char_loc.append((row_num, idx))
        row_num = row_num + 1

    return char_loc


char_loc = get_char_locations(matrix, char_set)


def check_left(matrix, current_location):
    row = current_location[0]
    col = current_location[1]
    left = matrix[row][col - 1]
    if re.match(r"\d", left):
        print(left)


def check_right(current_location):
    pass


def check_above(current_location):
    pass


def check_below(current_location):
    pass


# check neighbors for digits
def check_neighbor(matrix, char_loc):
    # get starting location
    starting_location = char_loc

    check_left(matrix, char_loc)
    # container for found digits
    # digit_block = []
    # if digit add to digit_block else end test

    # check above
    # if digit add to digit_block then check to the left and check to the right

    # check right

    # check below
    for loc in char_loc:
        row = loc[0]
        col = loc[1]
        up = matrix[row - 1][col]
        left = matrix[row][col - 1]
        right = matrix[row][col + 1]
        down = matrix[row + 1][col]
        # check above
        if re.match(r"\d", up):
            pass


check_neighbor(matrix, char_loc)


'''
references:
-----------
Find List Index of All Occurrences of an Element
https://datagy.io/python-list-find-all-index/

'''