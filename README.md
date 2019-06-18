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
 <ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: decimal; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Variables</span></li>
<ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: lower-alpha; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">user_selection</span></li>
<li style="list-style-type: lower-alpha; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">computer_selection</span></li>
<li style="list-style-type: lower-alpha; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Vocabulary = {&ldquo;R&rdquo;: &ldquo;ROCK&rdquo;, &ldquo;P&rdquo;: &ldquo;PAPER&rdquo;, &ldquo;S&rdquo;: &ldquo;SCISSORS&rdquo;}</span></li>
</ol>
<li style="list-style-type: decimal; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">User flow</span></li>
<ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: lower-alpha; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Input &ldquo;Do you want to play rock, paper, scissors? Y(Yes), N(No)&rdquo;</span></li>
<ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">if not [&ldquo;Y, N&rdquo;] </span></li>
<ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: decimal; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Print &ldquo;Sorry, you have failed reading the instructions. Please try harder.&rdquo;</span></li>
<li style="list-style-type: decimal; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">JUMP TO 2.a</span></li>
</ol>
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">if N </span></li>
<ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: decimal; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Print &ldquo;Thank you for playing rock, paper, scissors. Come back soon!&rdquo;</span></li>
<li style="list-style-type: decimal; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">END GAME</span></li>
</ol>
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">if Y</span></li>
<ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: decimal; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Computer selects randomly one of the choices</span></li>
<li style="list-style-type: decimal; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">input &ldquo;I picked my choice, please select one of these three choices, Rock, Paper, or Scissors. R(Rock), P(Paper), S(Scissors)&rdquo;</span></li>
<ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: lower-alpha; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">if not [&ldquo;R, P, S&rdquo;] </span></li>
<ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Print &ldquo;Sorry, you have failed spelling. Please try harder :D.&rdquo;</span></li>
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">JUMP TO 2.a.iii.2</span></li>
</ol>
<li style="list-style-type: lower-alpha; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">If user_selection is R and computer_selection is S</span></li>
<ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Print &ldquo;User selected Rock and computer selected Scissors.Rock beats Scissors! Congrats, you are better than a computer:D.&rdquo;</span></li>
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">JUMP TO 2.a</span></li>
</ol>
<li style="list-style-type: lower-alpha; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">If user_selection is P and computer_selection is R</span></li>
<ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Print &ldquo;User selected Paper and computer selected Rock. Paper beats Rock! Congrats, you are better than a computer:D.&rdquo;</span></li>
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">JUMP TO 2.a</span></li>
</ol>
<li style="list-style-type: lower-alpha; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">If user_selection is S and computer_selection is P</span></li>
<ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Print &ldquo;The user selected Scissors and computer selected paper. Scissors beats Paper! Congrats, you are better than a computer&rdquo;</span></li>
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">JUMP TO 2.a</span></li>
</ol>
<li style="list-style-type: lower-alpha; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">If user_selection is equal to computer_selection</span></li>
<ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Print &ldquo;The user selected the same as the computer. Let&rsquo;s redo the round&rdquo;</span></li>
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">JUMP TO 2.aiii.2</span></li>
</ol>
<li style="list-style-type: lower-alpha; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Else</span></li>
<ol style="margin-top: 0pt; margin-bottom: 0pt;">
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Print &ldquo;You lost to a computer. Please go try hard mode next time :(&rdquo; </span></li>
<li style="list-style-type: lower-roman; font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre;"><span style="font-size: 12pt; font-family: Arial; color: #000000; background-color: transparent; font-weight: 400; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">JUMP TO 2.a</span></li>
</ol>
</ol>

<p>&nbsp;</p>



