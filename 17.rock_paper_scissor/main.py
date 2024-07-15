import random

print("welcome to my rock paper scissor game")

_user_input = input('enter "r" for rock, "p" for paper and "s" for scissor: ')
_computer_input = random.choice([-1,0,1])

your_dict = {"r": -1, "p": 0, "s":1}
reverse_dict = {-1: "rock", 0:"paper",1:"scissor"}

user_input = reverse_dict[your_dict[_user_input]]
computer_input = reverse_dict[_computer_input]

print(f"you choose {user_input}, computer choose {computer_input}")

if(user_input == computer_input):
    print("it a draw")
else:
    if(user_input == "rock" and computer_input == "paper"):
        print("computer won")
    elif(user_input == "rock" and computer_input == "scissor"):
        print("you won")
    elif(user_input == "paper" and computer_input == "rock"):
        print("you won")
    elif(user_input == "paper" and computer_input == "scissor"):
        print("computer won")
    elif(user_input == "scissor" and computer_input == "rock"):
        print("computer won")
    elif(user_input == "scissor" and computer_input == "paper"):
        print("you won")
    
    
print("thanks for playing")