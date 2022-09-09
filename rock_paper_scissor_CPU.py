import random

def start_game():
    cpu_choices = ["Rock", "Paper", "Scissor"]
    cpu_choice = random.choice(cpu_choices)
    player_choice = input("Please Enter Rock, Paper, or Scissor ")

    if player_choice.capitalize() == "Rock":
        if cpu_choice.capitalize() == "Rock":
            print("Draw!")
        if cpu_choice.capitalize() == "Paper":
            print("CPU wins with Paper!")
        if cpu_choice.capitalize() == "Scissor":
            print("Player One wins with Rock!")

    elif player_choice.capitalize() == "Paper":
        if cpu_choice.capitalize() == "Rock":
            print("Player One wins with Paper!")
        if cpu_choice.capitalize() == "Paper":
            print("Draw!")
        if cpu_choice.capitalize() == "Scissor":
            print("CPU wins with Scissor!")

    elif player_choice.capitalize() == "Scissor":
        if cpu_choice.capitalize() == "Rock":
            print("CPU wins with Rock!")
        if cpu_choice.capitalize() == "Paper":
            print("Player One wins with Paper!")
        if cpu_choice.capitalize() == "Scissor":
            print("Draw!")

    else:
        print("Wrong input, please try again!")
        start_game()

start_game()

