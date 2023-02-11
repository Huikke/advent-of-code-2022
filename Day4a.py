count = 0

with open("Day4_Data.txt") as assigments:
    for assigment in assigments:
        # Separate the numbers and make them integer
        strings = assigment.strip().replace("-", ",").split(",")
        numbers = [eval(i) for i in strings]
        
        # Comparison
        if numbers[0] <= numbers[2] and numbers[1] >= numbers[3] or numbers[0] >= numbers[2] and numbers[1] <= numbers[3]:
            count += 1

print(count)