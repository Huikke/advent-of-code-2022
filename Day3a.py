total = 0

with open("Day3_Data.txt") as rucksacks:
    for rucksack in rucksacks:
        mistake = ""
        rucksack = rucksack.strip()
        middle = int(len(rucksack)/2)

        rucksack_comp1 = rucksack[0:middle]
        rucksack_comp2 = rucksack[middle:len(rucksack)]

        for i in rucksack_comp1:
            if i in rucksack_comp2:
                # ASCII stuff
                mistake = ord(i)
                if mistake > 96: #For a-z
                    mistake -= 96
                else: #For A-Z
                    mistake -= 38
                break

        total += mistake

print(total)