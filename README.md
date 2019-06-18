## RPS Game
A popular game, rock, paper, scissors, in Python.
RPS game 
Date:June 17, 2019
Version: 1.3


We are developing a game, played by many, called rock, paper, scissors.
Settings (How Game is Played)
The player will choose an option (rock, paper, or scissors) against a computer, who will have a randomly chosen pattern which will be adjusted based on if it thinks you have figured out the pattern. The computer will count down and at the end you must have chosen your option. You can not change your option.


What is the game?: Rock, Paper Scissors is a game in which a player chooses an option (rock, paper, or scissors) against another person or computer. Specific options beat other options: rock beats scissors, paper beats rock, scissors beats paper. If the same option is put, repeat the round until some player wins.

Characters (Who are the players)
The player will be matched up against a computer whose option is randomly generated.


Theme (Tips & Tricks )
Try to realize computers pattern 
Try to think of a strategy yourself
Learn from your mistakes
Think of a letter quickly so there is more matches for you to play
You can not change your answer so be confident with your answer


Age group: 3-12
Overview: The player will select an option (rock, paper or scissors) against a computer , whose option will be randomly chosen


# About
We wanted to make our first project relating to the game rock, paper, scissors. We are fifth graders going to sixth, and thought our first project should be this game. We are just starting to learn coding, and this is both of our first projects.


# Team
Jayesh Kankanala

I want to learn coding and am trying to be a software genius.
I am a 5th grader going into sixth and I am very interested in this project.
I am very inspired by STEM

Arjun Maganti
I want to be an engineer, also working with computer sciences.
I have just finished 5th grade, and am going into sixth.
I am excited about this project.
©2019, Jayesh Kankanala, Arjun Maganti 


----------------------------------------------------------------

# RPS Sequence Diagram

![Sequence Diagram](/mermaid-diagram-20190611162019.svg)

# RPS Flowchart

![Flowchart](/mermaid-diagram-20190611182108.svg)


# Pseudo Code
 Pseudo Code

```
Variables
user_selection
computer_selection
Vocabulary = {“R”: “ROCK”, “P”: “PAPER”, “S”: “SCISSORS”}
User flow
Input “Do you want to play rock, paper, scissors? Y(Yes), N(No)”
if not [“Y, N”] 
Print “Sorry, you have failed reading the instructions. Please try harder.”
JUMP TO 2.a
if N 
Print “Thank you for playing rock, paper, scissors. Come back soon!”
END GAME
if Y
Computer selects randomly one of the choices
input “I picked my choice, please select one of these three choices, Rock, Paper, or Scissors. R(Rock), P(Paper), S(Scissors)”
if not [“R, P, S”] 
Print “Sorry, you have failed spelling. Please try harder :D.”
JUMP TO 2.a.iii.2
If user_selection is R and computer_selection is S
Print “User selected Rock and computer selected Scissors.Rock beats Scissors! Congrats, you are better than a computer:D.”
JUMP TO 2.a
If user_selection is P and computer_selection is R
Print “User selected Paper and computer selected Rock. Paper beats Rock! Congrats, you are better than a computer:D.”
JUMP TO 2.a
If user_selection is S and computer_selection is P
Print “The user selected Scissors and computer selected paper. Scissors beats Paper! Congrats, you are better than a computer”
JUMP TO 2.a
If user_selection is equal to computer_selection
Print “The user selected the same as the computer. Let’s redo the round”
JUMP TO 2.aiii.2
Else
Print “You lost to a computer. Please go try hard mode next time :(” 
JUMP TO 2.a
```



