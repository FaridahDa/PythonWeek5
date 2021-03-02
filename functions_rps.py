import random

# get player choice
def get_player_choice (question ="\n Enter your choice (rock, paper or scissors):", possible_answers=["R", "P", "S"]) :
    while True:
        player_choice = input(question)
        if player_choice in possible_answers:
            return player_choice.upper()
        print(f"Your choice must be one of the following: { ','.join(possible_answers)}. \n")


def convert_player_choice(player_choice):
    full_words = {'R': 'rock',
                  'P': 'paper',
                  'S': 'scissors'
                  }
    return full_words[player_choice]

# computers choice, using random
def computer_choice():
    generate_choice = random.randint(0, 2)
    # convert numbers to computer choice
    if generate_choice == 0:
        return "R"
    elif generate_choice == 1:
        return "P"
    else:
        return "S"

# conver comp choice to words
def convert_computer_choice(generate_choice):
    full_words = {'R': 'rock',
                  'P': 'paper',
                  'S': 'scissors'
                  }
    return full_words[generate_choice]


# get score
