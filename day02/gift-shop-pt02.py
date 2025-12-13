with open ("input.txt") as puzzle_input:
    list_puzzle_input = puzzle_input.read().split(',')

id_ranges = []
for input in list_puzzle_input:
    start, end = input.split('-')
    id_ranges.append((int(start), int(end)))

invalid_id = 0
for start, end in id_ranges:
    for number in range(start, (end + 1)):
        s = str(number)
        for length in range(1, (len(s) // 2 + 1)):
            if (int(len(s) / (length))) * s[:(length)] == s:
                invalid_id += number
                break

print(invalid_id)