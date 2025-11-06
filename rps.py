# ----------------------- ROCK - PAPER - SCISSORS GAME----------------------
import random

print("Welcome to Rock Paper Scissors!")
print("Choose: rock, paper, or scissors")

# Get user choice
user_choice = input("Your choice: ").lower()

# Generate computer choice
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

print(f"Computer chose: {computer_choice}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose!")
else:
    print("Invalid choice! Please choose rock, paper, or scissors.")
