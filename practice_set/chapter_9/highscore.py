
# new_score = input("Enter your new score: ")

# with open("highscore.txt","r") as f:
#     highscore = f.read()
#     if(new_score > highscore):
#         with open("highscore.txt", "w") as n:
#             n.write(new_score)


import random

def game():
    print("you are playing the game")
    new_score = random.randint(1,100)
    with open("highscore.txt") as f:
        hiscore = f.read()

    if(hiscore == ""):
        hiscore = 0
    
    if(int(new_score) > int(hiscore)):
        with open("highscore.txt", "w") as n:
            n.write(str(new_score))
    return new_score


game()