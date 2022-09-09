def start_game():
    player_one = input("Player One: Enter Rock, Paper, or Scissor ")
    player_two = input("Player Two: Enter Rock, Paper, or Scissor ")

    if player_one.capitalize() == "Rock":
        if player_two.capitalize() == "Rock":
            print("Draw!")
        if player_two.capitalize() == "Paper":
            print("Player Two wins with Paper!")
        if player_two.capitalize() == "Scissor":
            print("Player One wins with Rock!")

    elif player_one.capitalize() == "Paper":
        if player_two.capitalize() == "Rock":
            print("Player One wins with Paper!")
        if player_two.capitalize() == "Paper":
            print("Draw!")
        if player_two.capitalize() == "Scissor":
            print("Player Two wins with Scissor!")

    elif player_one.capitalize() == "Scissor":
        if player_two.capitalize() == "Rock":
            print("Player Two wins with Rock!")
        if player_two.capitalize() == "Paper":
            print("Player One wins with Paper!")
        if player_two.capitalize() == "Scissor":
            print("Draw!")

    else:
        print("Wrong input, please try again!")
        start_game()

start_game()

