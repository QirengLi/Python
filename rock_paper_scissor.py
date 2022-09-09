player_one_wins = 0
player_two_wins = 0
draw = 0
score = f"Player One wins: {player_one_wins}\nPlayer Two wins: {player_two_wins}\nDraws: {draw}"

player_one = input("Player One: Enter Rock, Paper, or Scissor ")
player_two = input("Player Two: Enter Rock, Paper, or Scissor ")
print(f"Player One's choice {player_one}\nPlayer Two's choice {player_two}")

if player_one.capitalize() == "Rock":
    if player_two.capitalize() == "Rock":
        draw = 1
        print(f"Player One wins: {player_one_wins}\nPlayer Two wins: {player_two_wins}\nDraws: {draw}")
    if player_two.capitalize() == "Paper":
        player_two_wins + 1
        print(score)
    if player_two.capitalize() == "Scissor":
        player_one_wins + 1
        print(score)

elif player_one.capitalize() == "Paper":
    if player_two.capitalize() == "Rock":
        player_one_wins + 1
        print(score)
    if player_two.capitalize() == "Paper":
        draw + 1
        print(score)
    if player_two.capitalize() == "Scissor":
        player_two_wins + 1
        print(score)

elif player_one.capitalize() == "Scissor":
    if player_two.capitalize() == "Rock":
        player_two_wins + 1
        print(score)
    if player_two.capitalize() == "Paper":
        player_one_wins + 1
        print(score)
    if player_two.capitalize() == "Scissor":
        draw + 1
        print(score)

elif player_one.capitalize() == "Q" or player_two.capitalize() == "Q":
    print(f"Thanks for playing! Here are the scores for the game! {score}")
    quit()

else:
    print("Wrong input, please try again!")



