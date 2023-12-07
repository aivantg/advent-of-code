from pprint import pprint
import re

with open('input.txt') as f:
    input = f.read().splitlines()

with open('sample.txt') as f:
    sample = f.read().splitlines()

def process_input(input): 
    seeds = [int(num) for num in re.findall(r'seeds: ([\d\s]+)', input[0])[0].split()]
    i = 2
    maps = []
    current_map = []
    while i < len(input):
        if input[i] == '': 
            current_map.sort(key=lambda m: m['src'])
            maps.append(current_map)
            current_map = []
        elif ':' not in input[i]:
            groups = [int(num) for num in re.findall(r'(\d+)\s(\d+)\s(\d+)', input[i])[0]]
            current_map.append({'dest': groups[0], 'src': groups[1], 'len': groups[2]})
        i += 1

    current_map.sort(key=lambda m: m['src'])
    maps.append(current_map)
    return seeds, maps

def findResultForSeedInMap(seed, map): 
    for option in map: 
        start, end = option['src'], option['src'] + option['len']
        if seed >= start and seed < end: 
            return option['dest'] + seed - start
    return seed

def part1(input): 
    seeds, maps = process_input(input)
    for map in maps: 
        seeds = [findResultForSeedInMap(seed, map) for seed in seeds]

    return min(seeds)

print(f"Part 1 sample result: {part1(sample)}")
print(f"Part 1 input result: {part1(input)}")

log = print
print = pprint = lambda x: None 

def findResultRangesForSeedRangeInMap(seedRange, map): 
    result = []
    print("\nFinding result for seedrange")
    print(seedRange)
    print("Given map:")
    pprint(map)
    latestRange = seedRange
    for option in map: 
        start, len = option['src'], option['len']
        rangeStart, rangeLen = latestRange['start'], latestRange['len']
        end, rangeEnd = start + len, rangeStart + rangeLen
        print(f"map option: {option}, curRange: {latestRange}")


        # Portion of range that comes before the beginning of the option
        preOption = {'start': min(rangeStart, start), 'len': min(rangeEnd, start) - min(rangeStart, start)}
        inOption = {'start': max(start, rangeStart), 'len': min(rangeEnd, end) -  max(start, rangeStart)}
        postOption = {'start': max(end, rangeStart), 'len': rangeEnd - max(end, rangeStart)}

        print(f"preOption: {preOption}")
        print(f"inOption: {inOption}")
        print(f"postOption: {postOption}")


        if preOption['len'] > 0: 
            result.append(preOption)

        if inOption['len'] > 0: 
            result.append({'start': option['dest'] + (inOption['start'] - start), 'len': inOption['len']})

        if postOption['len'] > 0: 
            latestRange = postOption
        else: 
            print("Result:")
            pprint(result)
            return result

    result.append(latestRange)
    print("Result:")
    pprint(result)
    return result


def part2(input): 
    seeds_raw, maps = process_input(input)
    seedRanges = [{"start": seeds_raw[i], "len": seeds_raw[i + 1]} for i in range(len(seeds_raw)) if i%2 == 0]
    pprint("\nSTARTING SEED RANGES")
    
    pprint(seedRanges)
    pprint(maps)
    

    for map in maps: 
        print("\n\n**PROCESSING SEEDS**")
        pprint(seedRanges)
        pprint(map)
        newRanges = []
        for seedRange in seedRanges: 
            newRanges += findResultRangesForSeedRangeInMap(seedRange, map)
        seedRanges = newRanges

    print("\nFinal Seedranges")
    seedRanges.sort(key=lambda r: r['start'])
    pprint(seedRanges)
    return seedRanges[0]['start']

log(f"Part 2 sample result: {part2(sample)}")
log(f"Part 2 input result: {part2(input)}")


# Sad brute force solution to help me debug my code :'(
# note, requires reversal of src and dest parsing
# def part2_brute(input): 
#     seeds_raw, maps = process_input(input)
#     seedRanges = [{"start": seeds_raw[i], "len": seeds_raw[i + 1]} for i in range(len(seeds_raw)) if i%2 == 0]
    
#     maps.reverse()

#     cur = 69700000
#     while cur < 1000000000:
#         temp = cur
#         if cur % 1000000 == 0:
#             print(f"cur: {cur}")

#         for map in maps:
#             temp = findResultForSeedInMap(temp, map)
        
#         # check if temp is within any of the initial seed ranges
#         for seedRange in seedRanges: 
#             if temp >= seedRange['start'] and temp < seedRange['start'] + seedRange['len']: 
#                 return temp, cur
#         cur += 1
