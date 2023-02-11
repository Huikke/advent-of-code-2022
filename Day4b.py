count = 0

with open("Day4_Data.txt") as assigments:
    for assigment in assigments:
        # Separate the numbers and make them integer
        strings = assigment.strip().replace("-", ",").split(",")
        numbers = [eval(i) for i in strings]
        rang = range(numbers[0], numbers[1]+1)
        
        # Comparison (first part checks all except if they are inside the first part)
        if (numbers[2] in rang or numbers[3] in rang) or (numbers[0] >= numbers[2] and numbers[1] <= numbers[3]):
            count += 1

print(count)