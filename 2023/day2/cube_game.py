import re

with open('input.txt') as f:
    input = f.read()

with open('sample.txt') as f:
    sample = f.read()

# finds maximum # of blocks pulled of a given color in a game string
max_color_in_game = lambda game, color: max([int(val) for val in re.findall(fr'(\d*) {color}', game)], default=0)

# creates dictionary of color values given a game
cube_colors = ['red', 'green', 'blue']
process_game = lambda game: {color: max_color_in_game(game, color) for color in cube_colors}

# process games into ids and max color values = 
process_games = lambda input_str: {int(game[0]): process_game(game[1]) for game in re.findall(r'Game (\d*): (.*)', input_str)}

# Reads input and processes games into ids and max color values
games = process_games(input)
sample_games = process_games(sample)


# Part 1: find sum of ids of possible games
def sum_of_possible_games(games, given): 
    sum = 0
    for id, colors in games.items():
        sum += 0 if any([colors[color] > given[color] for color in cube_colors]) else id
    return sum 

given = {'red': 12, 'green': 13, 'blue': 14}
print (f"Part 1 result: {sum_of_possible_games(games, given)}")


# Part 2:   For each game find the minimum number of cubes to make the game valid
#           Return the sum of the each # of cube multiplied together

def sum_of_power_of_cubes(games):
    sum = 0
    for id, colors in games.items():
        power = 1
        for num in colors.values(): 
            power *= num
        sum += power
    return sum

print (f"Part 2 result: {sum_of_power_of_cubes(games)}")