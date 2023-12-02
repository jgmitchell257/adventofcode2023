# Advent of Code - Day 02
import aoc_utils

input_data = aoc_utils.load_input("day02/input")

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


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

def is_game_valid(game_data):
    for game in game_data:
        reveal = game_data[game]
        print(reveal)
        
        '''c = c.strip("\n")
        cube_details = c.split(",")
        for color in cube_details:
            p = color.strip()
            p = color.split()
            if p[1] == "red" and int(p[0]) < 12:
                pass
        print(game_number, cube_details)'''



game_data = get_game_data(input_data)
