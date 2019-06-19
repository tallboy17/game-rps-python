import random
import re

# variables
user_selection = "R"
computer_selection = "R"
vocabulary = {"R":"ROCK", "P":"PAPER", "S":"SCISSORS"}
play_input_pattern  = re.compile("^[R,P,S]{1,1}$")
user_input = "Y"

def computer_choice():
    return random.choice("RPS")

# user flow
while(1):
    user_input = input("Do you want to play rock, paper, scissors? Y(Yes), N(No)").upper()


    if user_input == "N":
        print ('Thank you for playing rock, paper, scissors.Come back soon!')
        break
    elif user_input == "Y":
        #computer selects randomly one of the choices
        computer_selection = computer_choice()

        user_selection = input ("I picked my choice, please select one of these three choices, Rock, Paper, or Scissors.R(Rock), P(Paper), S(Scissors)").upper()
        print (user_selection + " - " + computer_selection)
        if user_selection == "R" and computer_selection == "S":
            print("User selected Rock and computer selected Scissors.Rock beats Scissors! Congrats, you are better than a computer:D")
        elif user_selection == "P" and computer_selection == "R":
            print("User selected Paper and computer selected Rock. Paper beats Rock! Congrats, you are better than a computer:D")
        elif user_selection == "S" and computer_selection == "P":
            print("The user selected Scissors and computer selected paper. Scissors beats Paper! Congrats, you are better than a computer:D")
        elif user_selection == computer_selection:
            print(f"The user selected the  as the computer [computer = {vocabulary[computer_selection]} and user = {vocabulary[user_selection]} ]. Let’s redo the round")
        else:
            if play_input_pattern.search(user_selection):
                print( f'You lost to a computer [computer = {vocabulary[computer_selection]} and user = {vocabulary[user_selection]} ]. Please go try hard mode next time :(')
            else:
                print("Sorry, you have failed reading the instructions. Please try harder.")
    else:
        print("Sorry, you have failed reading the instructions. Go to reading classes.")

