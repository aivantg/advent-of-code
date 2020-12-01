import time

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

entries = []
with open('input.txt') as input: 
  for line in input: 
    entries.append(int(line))

entry_set = set(entries)
print(f"Starting with {len(entries)} entries...\n")

@time_it
def two_sum(): 
  # Find 2 matching pairs
  start = time.time()
  for entry in entries: 
    matching_entry = 2020 - entry
    if matching_entry in entry_set: 
      print(f"Found pair: {entry} & {matching_entry}\nAnswer: {entry * matching_entry}")
      return

two_sum()

# Find 3 matching triplets
@time_it
def three_sum(): 
  for entry1 in entries: 
    sum_left = 2020 - entry1
    for entry2 in entries: 
      matching_entry = sum_left - entry2
      if matching_entry in entry_set: 
        print(f"Found triplet: {entry1}, {entry2}, & {matching_entry}\nAnswer: {entry1*entry2*matching_entry}")
        return


three_sum()