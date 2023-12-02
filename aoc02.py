# Advent of Code - Day 02
import aoc_utils

# load input
input_data = aoc_utils.load_input("day02/input")


# Get the details of each game
def get_game_data(d):
    my_data = {}
    for game in d:
        game = game.strip("\n")
        game_details = game.split(":")
        game_number = game_details[0]
        game_number = game_number.split()
        game_number = game_number[1]
        game_reveal = game_details[1].split(";")
        my_data[int(game_number)] = game_reveal
    return my_data


game_data = get_game_data(input_data)


# Test each game for valid results
def remove_invalid(game_data):
    check = []
    for game in game_data:
        maybe_valid = True
        reveal = game_data[game]
        for r in reveal:
            r = r.split(",")
            for n in r:
                n = n.split()
                if int(n[0]) > 14:
                    maybe_valid = False
                if int(n[0]) > 12 and n[1] == "red":
                    maybe_valid = False
                if int(n[0]) > 13 and n[1] == "green":
                    maybe_valid = False
                
        if maybe_valid:
            check.append(game)
    return check


possible = remove_invalid(game_data)


# Check possible trult valid results
def check_possible(possible):
    total = 0
    for p in possible:
        total = total + int(p)
    print(total)


check_possible(possible)

# Part 2
# Find the minimum cubes for each reveal

def get_cubes(game_data):
    total_sum_of_powers = 0
    for game in game_data:
        red = 0
        blue = 0
        green = 0
        reveals = game_data[game]
        for hand in reveals:
            ind = hand.split(",")
            for cube_set in ind:
                cube_count = cube_set.split()
                count = int(cube_count[0])
                if "red" in cube_count:
                    if count > red:
                        red = count
                if "blue" in cube_count:
                    if count > blue:
                        blue = count
                if "green" in cube_count:
                    if count > green:
                        green = count
        total_sum_of_powers = total_sum_of_powers + (red * blue * green)
    print(total_sum_of_powers)

get_cubes(game_data)