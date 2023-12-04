# Read trebuchet_input.txt file as array of lines
with open('input.txt') as f:
    trebuchetInput = f.readlines()

def trebuchet_pt1(input): 
    digits = [[int(char) for char in line if char.isnumeric()] for line in input]
    calibrationValues = [row[0]*10 + row[-1] for row in digits]
    return sum(calibrationValues)

result = trebuchet_pt1(trebuchetInput)
print(f"Result Pt1: {result}")

### part two
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven' : 7, 'eight': 8, 'nine': 9}
validDigitWords = numbers.keys()

# takes string and parses out all the digits
def parse_digits(row): 
    digits = []
    i = 0
    while i < len(row):
        # check regular digits: 
        if row[i].isnumeric(): 
            digits.append(int(row[i]))
            i+=1
            continue
        
        # check for word digits
        for word in validDigitWords: 
            if row[i:].startswith(word): 
                digits.append(numbers[word])
                break
        
        i += 1
    return digits


def trebuchet_pt2(input): 
    rowDigits = [parse_digits(line) for line in input]
    calibrationValues = [row[0]*10 + row[-1] for row in rowDigits]
    return sum(calibrationValues)

result = trebuchet_pt2(trebuchetInput)
print(f"Result Pt2: {result}")