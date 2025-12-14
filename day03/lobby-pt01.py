with open ("input.txt") as puzzle_input:
    banks = puzzle_input.read().splitlines()

max_joltage = []
for bank in banks:
    list_bank = list(bank)
    if bank.index(max(list_bank)) == (len(bank) - 1):
        highest_num2 = max(list_bank)
        list_bank.remove(max(list_bank))
        highest_num1 = max(list_bank)
        max_joltage.append((highest_num1, highest_num2))
    else:
        highest_num1 = max(list_bank)
        idx_num1 = list_bank.index(highest_num1)
        highest_num2 = max(list_bank[(idx_num1+1):])
        max_joltage.append((highest_num1, highest_num2))

total_joltage = 0
for first, second in max_joltage:
    battery_pair = int(first + second)
    total_joltage += battery_pair

print(total_joltage)


