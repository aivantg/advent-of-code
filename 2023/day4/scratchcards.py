from pprint import pprint
import re

with open('input.txt') as f:
    input = f.read().splitlines()

with open('sample.txt') as f:
    sample = f.read().splitlines()

def process_card(card_str): 
    groups = re.findall(r'Card\s+(\d+): ([\d\s]+) \| ([\d\s]+)', card_str)[0]
    card_id = groups[0]
    winning_numbers = set(groups[1].split())
    card_numbers = groups[2].split()
    return card_id, winning_numbers, card_numbers

def num_winning(card_str): 
    _, winning_numbers, card_numbers = process_card(card_str)
    return sum([1 for num in card_numbers if num in winning_numbers])
    
def score_card(card_str): 
    wins = num_winning(card_str)
    return pow(2, wins - 1) if wins else 0


def part1(cards): 
    return sum([score_card(card) for card in cards])

print(f"Part 1 sample result: {part1(sample)}")
print(f"Part 1 input result: {part1(input)}")

def part2(cards): 
    copy_dict = {}
    for i, card in enumerate(cards): 
        score = num_winning(card)
        for j in range(score): 
            copy_dict[i + j + 2] = copy_dict.get(i + j + 2, 1) + copy_dict.get(i + 1, 1)

    return sum([copy_dict.get(i + 1, 1) for i in range(len(cards))])

print(f"Part 2 sample result: {part2(sample)}")
print(f"Part 2 input result: {part2(input)}")