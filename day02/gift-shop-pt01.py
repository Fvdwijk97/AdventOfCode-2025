# ====================================
# STAPPENPLAN
# 1. Copy paste puzzle input to input.txt file
# 2. Read puzzle input into program
# 3. Convert puzzle input into list of tuples, each tuple representing an ID-range (start, end)
# 4. Loop through numbers of each ID-range including both numbers
# 5. Check if each number contains at least two of the same digits, if so the number is an invalid ID
# 6. Sum up the value of each invalid ID
# ====================================

# 2
with open ("input.txt") as puzzle_input:
    list_puzzle_input = puzzle_input.read().split(',')

# 3
id_ranges = []
for input in list_puzzle_input:
    start, end = input.split('-')
    id_ranges.append((int(start), int(end)))
#print(id_ranges[:3])

# 4, 5, 6
invalid_id = 0
for start, end in id_ranges:
    for number in range(start, (end + 1)):
        s = str(number)
        if len(s) % 2 == 0:
            half = len(s) // 2
            if s[:half] == s[half:]:
                invalid_id += number

print(invalid_id)
