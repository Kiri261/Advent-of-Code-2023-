#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:13:09 2023

@author: kirishanakiritharan
"""

def check_possible_games(input_data, red_count, green_count, blue_count):
    possible_games = []
    
    for line in input_data:
        game_info = line.split(': ')[1].split('; ')
        possible = True
        
        for subset in game_info:
            cubes = subset.split(', ')
            cube_count = {cube.split()[1]: int(cube.split()[0]) for cube in cubes}
            
            if cube_count.get('red', 0) > red_count or cube_count.get('green', 0) > green_count or cube_count.get('blue', 0) > blue_count:
                possible = False
                break
        
        if possible:
            game_id = int(line.split(':')[0].split()[1])
            possible_games.append(game_id)
    
    return possible_games

# Read game data from a file
file_path = '/Users/kirishanakiritharan/Desktop/input2'  # Replace 'games_input.txt' with your file name/path
with open(file_path, 'r') as file:
    games_input = file.readlines()

# Cube counts
red_count = 12
green_count = 13
blue_count = 14

possible_games = check_possible_games(games_input, red_count, green_count, blue_count)
print("Possible games:", possible_games)
print("Sum of IDs of possible games:", sum(possible_games))
