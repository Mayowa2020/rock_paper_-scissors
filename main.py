import random
print()

print("Welcome to Rock Paper Scissors!")
print("---------------------------------")

options = {
    "r" : "rock",
    "p" : "paper",
    "s": "scissors",
    }

keys = options.keys()

# Convert to list
keys = list(options.keys())

print()

print("These are the available options:")
print()
print("1. R for Rock")
print("2. P for Paper")
print("3. S for Scissors")
print("Q to quit game")

print()

while True:
   
    user_input = input("Enter your Choice: R, P, S or Q to quit: ").lower()
   
    print()

    if user_input == "q":
        break
    if user_input not in keys:
        print(f"Error: Unknown option. \n")
        continue
    
    # Generate a computer pick
    computer_pick = random.choice(keys)

    print(f"\nYou chose {user_input}, computer chose {computer_pick}.\n")
    
    if user_input == computer_pick:
        print(f"Both players selected {user_input}. It's a tie!\n")
        continue         
        
    elif user_input == "r" and computer_pick == "s" or user_input == "p" and computer_pick == "r" or user_input == "s" and computer_pick == "p":
        print("You win!")
      

    else: print("You lose!")
    print()

print("Game over! Thank you for playing!")
print()