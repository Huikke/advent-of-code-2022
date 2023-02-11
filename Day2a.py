score = 0

with open("Day2_Data.txt") as games:
    for game in games:

        if game[2] == "X":
            score += 1
            if game[0] == "A":
                score += 3
            if game[0] == "C":
                score += 6
        if game[2] == "Y":
            score += 2
            if game[0] == "B":
                score += 3
            if game[0] == "A":
                score += 6
        if game[2] == "Z":
            score += 3
            if game[0] == "C":
                score += 3
            if game[0] == "B":
                score += 6
    
print(score)