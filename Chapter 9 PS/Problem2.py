import random

def game():
    print("You are playing a game...")
    score = random.randint(2,62)
    #  fetch the hiscore from file 
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score is {score}")

    if (score > hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return score

game()