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
    entries.append(line)

print(f"Found {len(entries)} entries!")


def process_entry(entry):
    s1 = entry.split(': ')
    rule, password = s1[0], s1[1]
    s2 = rule.split(' ')
    limits, letter = s2[0], s2[1]
    s3 = limits.split('-')
    low, high = s3[0], s3[1]
    return int(low), int(high), letter, password

def validate_password_1(low, high, letter, password):
    count = 0
    for char in password:
        count += 1 if letter == char else 0
    return (count >= low and count <= high)

def validate_password_2(low, high, letter, password):
    idx_1, idx_2 = low - 1, high - 1
    val_1, val_2 = password[idx_1] == letter, password[idx_2] == letter
    return (val_1 or val_2) and not (val_1 and val_2)


@time_it
def validate_passwords(entries, method):
    valid_passwords = 0
    for entry in entries:
        low, high, letter, password = process_entry(entry)
        if method == 1:
            valid = validate_password_1(low, high, letter, password)
        elif method == 2:
            valid = validate_password_2(low, high, letter, password)

        if valid:
            valid_passwords += 1
            
    print(f"Found {valid_passwords} valid passwords using method {method}")
    return valid_passwords

validate_passwords(entries, 1)
validate_passwords(entries, 2)
