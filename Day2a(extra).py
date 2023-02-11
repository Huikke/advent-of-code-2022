score = 0
wins = 0
ties = 0
losses = 0
rocks = 0
papers = 0
scissors = 0

with open("Day2_Data.txt") as games:
    for game in games:

        if game[2] == "X":
            score += 1
            rocks += 1
            if game[0] == "A":
                score += 3
                ties += 1
            elif game[0] == "C":
                score += 6
                wins += 1
            else:
                losses += 1
        if game[2] == "Y":
            score += 2
            papers += 1
            if game[0] == "B":
                score += 3
                ties += 1
            elif game[0] == "A":
                score += 6
                wins += 1
            else:
                losses += 1
        if game[2] == "Z":
            score += 3
            scissors += 1
            if game[0] == "C":
                score += 3
                ties += 1
            elif game[0] == "B":
                score += 6
                wins += 1
            else:
                losses += 1
    
print("score:", score)
print("wins:", wins)
print("ties:", ties)
print("losses:", losses)
print("rocks:", rocks)
print("papers:", papers)
print("scissors:", scissors)