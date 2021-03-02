#!/usr/bin/env python
import functions_rps

# welcome to game
print("------------------------------------")
print("Welcome to Rock, Paper, Scissors!")
print("-------------------------------------")

while True:
    user_choice = functions_rps.get_player_choice()
    user_choice_converted = functions_rps.convert_player_choice(user_choice)
    comp_choice = functions_rps.computer_choice()
    comp_choice_converted = functions_rps.convert_player_choice(comp_choice)
    print(f"\n You chose {user_choice_converted}, computer chose {comp_choice_converted} \n")

    # the game
    if user_choice == comp_choice:
        print(f"Both players selected {user_choice_converted}. It's a tie!")
    elif user_choice == "R":
        if comp_choice == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == "P":
        if comp_choice == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == "S":
        if comp_choice == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    #play_again = input("Play again? (y/n: ")
    #if play_again.upper() != "y":
        #break




