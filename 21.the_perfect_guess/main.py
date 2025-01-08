from random import randint

number = randint(1, 100)

users = {
    "user_1": 0,
    "user_2": 0
}

def get_result():
    print("\nGame Over!")
    print(f"Total attempts - User 1: {users['user_1']}, User 2: {users['user_2']}")
    
    if users["user_1"] < users["user_2"]:
        print("User 1 wins with fewer attempts!")
    elif users["user_1"] > users["user_2"]:
        print("User 2 wins with fewer attempts!")
    else:
        print("It's a tie!")

def user_2_turn():
    global number
    print("\nUser 2's turn")
    user2_input = int(input("Enter your guess between 1 and 100: "))
    users["user_2"] += 1

    if user2_input > number:
        print("Guess a smaller number.")
        user_2_turn()
    elif user2_input < number:
        print("Guess a greater number.")
        user_2_turn()
    else:
        print("User 2 guessed it right!")
        get_result()

def user_1_turn():
    global number
    print("\nUser 1's turn")
    user1_input = int(input("Enter your guess between 1 and 100: "))
    users["user_1"] += 1

    if user1_input > number:
        print("Guess a smaller number.")
        user_1_turn()
    elif user1_input < number:
        print("Guess a greater number.")
        user_1_turn()
    else:
        print("User 1 guessed it right!")
        number = randint(1, 100)
        user_2_turn()

def start_game():
    print("Game starting...")
    print("Rules: Try to guess the number in the fewest attempts.")
    user_1_turn()

start_game()
