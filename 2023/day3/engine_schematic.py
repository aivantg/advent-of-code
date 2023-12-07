from pprint import pprint
import re

with open('input.txt') as f:
    input = f.read().splitlines()

with open('sample.txt') as f:
    sample = f.read().splitlines()

def symbol_at_loc(coord, schema):
    x, y = coord
    width = len(schema[0])
    height = len(schema)

    if x < 0 or x == width or y < 0 or y == height: 
        return False 
    
    char = schema[y][x]
    return char if not (char.isnumeric() or char == '.') else None
    

def get_locs_around_num(num_loc): 
    x_span = num_loc[0]
    y = num_loc[1]

    possible_locations = []

    # check row above
    possible_locations += [(x, y - 1) for x in range(x_span[0] - 1, x_span[1] + 1)]

    # check row below
    possible_locations += [(x, y + 1) for x in range(x_span[0] - 1, x_span[1] + 1)]

    # check left and right
    possible_locations += [(x_span[0] - 1, y), (x_span[1], y)]
    return possible_locations

# part 1
def find_engine_parts(schema): 
    all_nums = []
    for i, row in enumerate(schema): 
        for match in re.finditer(r'(\d*)', row):
            if match.group(): 
                all_nums.append((int(match.group()), (match.span(), i)))

    sum = 0
    for num, num_loc in all_nums: 
        locations = get_locs_around_num(num_loc)
        symbols = [symbol_at_loc(loc, schema) for loc in locations]
        sum += num if any(symbols) else 0 

    return sum
        
print(f"Result for part 1 sample: {find_engine_parts(sample)}")
print(f"Result for part 1 input: {find_engine_parts(input)}")
    

# part 2
def find_gear_ratios(schema): 
    all_nums = []
    for i, row in enumerate(schema): 
        for match in re.finditer(r'(\d*)', row):
            if match.group(): 
                all_nums.append((int(match.group()), (match.span(), i)))

    gears = {}
    sum = 0
    for num, num_loc in all_nums: 
        locations = get_locs_around_num(num_loc)
        for loc in locations: 
            if symbol_at_loc(loc, schema) == '*': 
                gears[loc] = gears.get(loc, []) + [num]
        
    for loc, nums in gears.items(): 
        if len(nums) == 2: 
            sum += nums[0] * nums[1]
        
    return sum


print(f"Result for part 2 sample: {find_gear_ratios(sample)}")
print(f"Result for part 2 input: {find_gear_ratios(input)}")