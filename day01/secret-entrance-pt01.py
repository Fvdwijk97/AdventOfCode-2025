# 1. tekstbestand met input AdventOfCode inlezen
# 2. lijst maken van alle elementen in tekstbestand AdventOfCode
# 3. tuples maken van alle elementen in de lijst
# 4. beginnen bij 50
# 5. range van 0-99
# 6. if R in tuple naar hoge nummers (plus)
# 7. if L in tuple naar lage nummers (min)

with open ("input.txt") as input_file:
    attached_doc = input_file.read().splitlines() # lijst maken van alle rotations in attached document.
    attached_doc = [(rotation[0], int(rotation[1:])) for rotation in attached_doc] # van alle rotations tuples maken.
 #   print(attached_doc[:5])

aantal_cijfers = range(0,100) # 0 t/m 99
dial = 50 # dial start op 50
count_zeros = 0

for rotation in attached_doc:
    steps = rotation[1]
    if "R" in rotation:
        dial = abs((dial + steps) % 100)
        if dial == 0:
            count_zeros += 1
    elif "L" in rotation:
        dial = abs((dial - steps) % 100)
        if dial == 0:
            count_zeros += 1

print(count_zeros)

