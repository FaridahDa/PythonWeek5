#!/usr/bin/env python
import random

while True :
    possible_choices = ["rock", "paper", "scissors"]
    player_choice = input("Please enter a choice (rock, paper or sicssors: \n")
    computer_choice = random.choice(possible_choices)
    print(f"\n you chose {player_choice} , computer chose {computer_choice}. \n")

    if player_choice == computer_choice:
        print(f"Both players selected {player_choice}. It's a tie!")