total = 0

with open("Day3_Data.txt") as rucksacks:
    for rucksack in rucksacks:
        badge = ""
        elf1_rs = rucksack.strip()
        # get two next lines and also get for loop forward, idk it works
        elf2_rs = rucksacks.readline()
        elf3_rs = rucksacks.readline()

        for i in elf1_rs:
            if i in elf2_rs and i in elf3_rs:
                # ASCII stuff
                badge = ord(i)
                if badge > 96: #For a-z
                    badge -= 96
                else: #For A-Z
                    badge -= 38

        total += badge

print(total)