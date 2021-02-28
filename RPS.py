p1 = 'you'
p2 = 'computer'
choices = ["R", "P", "S"]

import random

# computer generated choice
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

def rps():
   p1 = players_choice()
   p2 = computer_choice()
   print(p1, p2)
   beats = {'R': 'S', 'P': 'R', 'S': 'P'}
   if beats[p1] == p2:
      print('Player 1 wins!!')
    if beats[p2] == p1:
      print('player 2 wins!!')
    print('Draw')

rps()
