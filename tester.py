#!/usr/bin/env python
import random
# create list of items
choices = ["R", "P", "S"]
player_winning_combinations = ["RP", "SR", "PS"]

# # computer generated choice
def computer_choice():
    generate_choice = random.randint(0, 2)
    if generate_choice == 0:
        return "R"
    elif generate_choice == 1:
        return "P"
    else:
        return "S"

# make sure user input is valid
def players_choice():
    person_choice = input("Enter your choice:\n").upper()
    while person_choice not in choices:
        person_choice = input("Please enter correct choice: \n").upper()
    return person_choice


def find_winner():
    comp = computer_choice()
    player = players_choice()
    print(comp, player)
    if comp == player:
        print("Draw")
    elif comp + player in player_winning_combinations:
        print("You win with", player)
        return "win"
    else:
        print("You lose, computer wins with", comp)
        return "lose"

