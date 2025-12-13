with open ("input.txt") as input_file:
    attached_doc = input_file.read().splitlines() # lijst maken van alle rotations in attached document.
    attached_doc = [(rotation[0], int(rotation[1:])) for rotation in attached_doc] # van alle rotations tuples maken.

aantal_cijfers = range(0,100)
dial = 50
count_zeros = 0

for dir, steps in attached_doc:
    if dir == "R":
        dial = abs((dial + steps) % 100)
        if dial == 0:
            count_zeros += 1
    elif dir == "L":
        dial = abs((dial - steps) % 100)
        if dial == 0:
            count_zeros += 1

print(count_zeros)

