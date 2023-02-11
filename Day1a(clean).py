most_calory = 0
current_calory = 0

with open("Day1_Data.txt") as calories:    
    for calory in calories:
        calory = calory.strip()

        if calory == "":
            if current_calory > most_calory:
                 most_calory = current_calory
            current_calory = 0
        else:
            calory = int(calory)
            current_calory += calory

print(most_calory)