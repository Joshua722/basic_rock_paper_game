import random

def play_rock_paper_scissors():
    choices = ["Rock", "Paper", "Scissors"]

    computer_input = random.choice(choices)
    player_input = input("Rock,Paper,Scissors?\n").capitalize()

    print("The computer chooses! " + computer_input)
    print("You chose " + player_input)

    if computer_input == player_input: 
        print("ITS A DRAW!!!!!")
    elif (
        (computer_input == "Rock" and player_input == "Scissors") or
        (computer_input == "Scissors" and player_input == "Paper") or
        (computer_input == "Paper" and player_input == "Rock")
    ):
        print("THE COMPUTER WINS!!!")
    else:
        print("YOU WIN!!!!")

play_rock_paper_scissors()    