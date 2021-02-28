from random import randomint
player_choices = ["Rock", "paper", "siccsors"]

#computer choices
computer = player

def rps(p1, p2):
    user_choice = input("Please enter your choice:")
    beats = {'rocks': 'siccsors', 'paper': 'rock', 'siccsors': 'paper' }
    if beats[p1] == p2:
        return 'Player 1 wins!!'
    if beats[p2] == p1:
        return 'player 2 wins!!'
    return 'Draw'
