with open ("input.txt") as input_file:
    attached_doc = input_file.read().splitlines() # lijst maken van alle rotations in attached document.
    attached_doc = [(rotation[0], int(rotation[1:])) for rotation in attached_doc] # van alle rotations tuples maken.

aantal_cijfers = range(0,100) # 0 t/m 99
dial = 50 # dial start op 50
count_zeros = 0

for direction, steps in attached_doc:
    for x in range(steps):

        if direction == "R":
            dial += 1
        elif direction == "L":
            dial -= 1

        if dial == -1 or dial == 100:
            dial %= 100

        if dial == 0:
            count_zeros += 1

print(count_zeros)






