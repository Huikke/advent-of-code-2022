most_calory_1st = 0
most_calory_2nd = 0
most_calory_3rd = 0
current_calory = 0

with open("Day1_Data.txt") as calories:
    for calory in calories:
        calory = calory.strip()

        if calory == "":
            if current_calory > most_calory_3rd:
                most_calory_3rd = current_calory
                if current_calory > most_calory_2nd:
                    most_calory_2nd, most_calory_3rd = most_calory_3rd, most_calory_2nd
                    if current_calory > most_calory_1st:
                        most_calory_1st, most_calory_2nd = most_calory_2nd, most_calory_1st

            current_calory = 0
        else:
            calory = int(calory)
            current_calory += calory

print(most_calory_1st + most_calory_2nd + most_calory_3rd)