import time
from pprint import pprint

def time_it(func):
    def wrapper(*arg, **kw):
        start = time.time()
        result = func(*arg, **kw)
        end = time.time()
        # time_taken = (int((end - start)*10000000)/float(10000000))
        time_taken = end - start
        print(f"Finished running in  {time_taken} seconds\n")
        return result
    return wrapper

slopes = []
with open('input.txt') as input: 
  for line in input:
      slopes.append(list(line.strip()))

def travel_to_bottom(slopes, trajectory):
    right, down = trajectory
    height, width = len(slopes), len(slopes[0])
    x_pos, y_pos = 0, 0
    
    trees, steps = 0, 0
    while y_pos < height:
        cur_value = slopes[y_pos][x_pos]
        
        if cur_value == '#':
            trees += 1

        x_pos = (x_pos + right) % width # cycle around
        y_pos += down
        steps += 1
    
    print(f"Hit {trees} trees over {steps} steps using trajectory: {trajectory}")
    return trees

trajectories = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
answers = [travel_to_bottom(slopes, traj) for traj in trajectories]

result = 1
for answer in answers:
    result *= answer

print(result)



