# Rock - Paper - Scissor game
# Rock > Scissor, Scissor > Paper, Paper > Rock

import random

input("Press Enter to start!")
print("")

possible_choices = ["rock", "paper", "scissor"]  # Making possible choices list for rock, paper, scissor

user_wins = 0  # variable for user points
computer_wins = 0  # variable for cpi points
print("")

while True:  # Put the conditions into a loop
    computer_choice = random.choice(possible_choices)  # Choosing computer choice randomly
    user_choice = input("Enter your choice (rock, paper, scissor): ").lower()  # Asking user choice for rock, paper or scissor
    print("")
# Making conditions for the game
    if computer_choice == "rock":
        print("Computer choice:", computer_choice, "\nUser choice:", user_choice)
        if user_choice == "rock":
            print("")
            print("Draw")
        elif user_choice == "paper":
            print("")
            print("User win!")
            user_wins += 1
        elif user_choice == "scissor":
            print("")
            print("Computer wins!")
            computer_wins += 1
    elif computer_choice == "paper":
        print("Computer choice:", computer_choice, "\nUser choice:", user_choice)
        if user_choice == "paper":
            print("")
            print("Draw")
        elif user_choice == "rock":
            print("")
            print("Computer wins!")
            computer_wins += 1
        elif user_choice == "scissor":
            print("")
            print("User win!")
            user_wins += 1
    elif computer_choice == "scissor":
        print("Computer choice:", computer_choice, "\nUser choice:", user_choice)
        if user_choice == "scissor":
            print("")
            print("Draw")
        elif user_choice == "rock":
            print("")
            print("User win!")
            user_wins += 1
        elif user_choice == "paper":
            print("")
            print("Computer wins!")
            computer_wins += 1
# printing user / cpu wins after every game
    print("")
    print("You have " + str(user_wins) + " win(s).")  # 
    print("Computer has " + str(computer_wins) + " win(s).")
    print("")
# play again, if "y", next game, else quite game
    repeat = input("Play again? (y / n) ").lower()
    if repeat != "y":
        break

    print("\n----------------\n")



