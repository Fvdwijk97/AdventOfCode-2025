def zoekgebied_bepalen(lst, tot_en_met):
    """Geeft het deel van de lijst terug, waarin het (volgende) hoogste cijfer opgezocht mag worden"""
    return lst[:tot_en_met]

def tot_en_met_bepalen(lijst, uitgesloten):
    """Zorgt ervoor dat we het minimum aantal cijfers overhouden om overige hoogste cijfers te bepalen """
    return len(lijst) - uitgesloten

with open ("input.txt") as puzzle_input:
    banks = list(puzzle_input.read().splitlines())

antwoord = 0
for bank in banks:
    battery_joltages = [int(x) for x in bank]
    uitgesloten = 11 # Resultaat moet 12 cijfers bevatten, dus 11 aan einde uitsluiten voor eerste keuze
    hoogste_joltage = "" # Opbouwen 12-cijferige getallen

    for num in range(1, 13):
        # Toegestane zoekgebied & hoogste cijfer hierin bepalen:
        tot_en_met = tot_en_met_bepalen(battery_joltages, uitgesloten)
        zoekgebied = zoekgebied_bepalen(battery_joltages, tot_en_met)
        hoogste_cijfer = max(zoekgebied)

        # Zoekgebied voor volgende iteratie aanpassen:
        uitgesloten -= 1
        idx = (battery_joltages.index(hoogste_cijfer) + 1)
        battery_joltages = battery_joltages[(idx):]

        # Hoogste getal per iteratie toevoegen tot 12 cijferig getal bereikt is:
        hoogste_joltage += str(hoogste_cijfer)

        # Zodra 12 cijferig getal opgebouwd is, waarde van dit getal optellen bij antwoord:
        if len(hoogste_joltage) == 12:
            antwoord += int(hoogste_joltage)

print(antwoord)
