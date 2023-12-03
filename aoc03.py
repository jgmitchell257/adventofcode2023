# Advent of Code - Day 3
import re
import aoc_utils

original_data = aoc_utils.load_input("day03/input")


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


def get_char_set(matrix_data):
    char_set = []
    for row in matrix_data:
        for character in row:
            if not re.match(r"\d|\.", character):
                char_set.append(character)

    return list(set(char_set))


char_set = get_char_set(matrix)


def get_char_locations(matrix, char_set):
    # find location in the matrix
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


def find_neighbor(char_loc):
    for loc in char_loc:
        row = loc[0]
        col = loc[1]


find_neighbor(char_loc)
