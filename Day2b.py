score = 0

with open("Day2_Data.txt") as games:
    for game in games:

        if game[2] == "X":
            if game[0] == "A":
                score += 3
            if game[0] == "B":
                score += 1
            if game[0] == "C":
                score += 2
        if game[2] == "Y":
            score += 3
            if game[0] == "A":
                score += 1
            if game[0] == "B":
                score += 2
            if game[0] == "C":
                score += 3
        if game[2] == "Z":
            score += 6
            if game[0] == "A":
                score += 2
            if game[0] == "B":
                score += 3
            if game[0] == "C":
                score += 1
    
print(score)