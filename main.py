import random 

print("Welcome to Rock Paper Scissors!")
print("---------------------------------")

# # Set up variables

# user_wins = 0
# computer_wins = 0
# tie = 0


options = ["rock", "paper", "scissors"]


# print("These are the possible options")
# print("1. R for Rock")
# print("2. P for Paper")
# print("3. S for Scissors")
# print("Q to quit game")



while True:

    user_input = input("\n Pick the any of the possible options: Rock, Paper, Scissors or Q to quit: ").lower()
       
    if user_input == "q":
        break
    if user_input not in options:
        print("Error: Unknown option")
        # continue

    # Generate a computer pick
    computer_pick = random.choice(options)
    # random_number = random.randint(0, 2)
    # #rock: 0, paper: 1, scissors: 2
    # computer_pick = options[random_number]
    print("Computer picked: " + computer_pick + ".")
    
    if user_input == computer_pick:
        print("Tie!")
        # continue

    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")

    else: print("You lost!")

print("Game over! Thank you for playing!")
