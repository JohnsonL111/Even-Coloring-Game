# Even-Coloring-Game 
<br>
Scuffed CMPT 120 Final Project 😫
<br>
# How-to-Play <br> 
-Select 1 of the 3 starter boards (displayed as a square matrix)
<br>
 <br>&nbsp;&nbsp;&nbsp;&nbsp;C0    C1    C2 <br> 
R0&nbsp; 0 &nbsp; 3 &nbsp;2 <br>
R1&nbsp; 1 &nbsp; 5 &nbsp;4 <br>
R2&nbsp; 0 &nbsp; 0 &nbsp;1 <br> 
<br> 
Figure 1. Starter Board 3 (CX = Column X | RX = Row X)
<br> 
-Select # of games you want to play
<br>
-Select # of turns (max # of turns is: # of rows - 1) eg. 4 row board = 3 turns max
<br>
-The user can change 1 digit on the board to any # between 0-9.
<br>
-Game ends when all turns are used.
<br>

<b> Objective: Make all rows and columns add up to an even number. </b> 
<br> 

# Point Calculuation: 
<br>
-The sum of each row and column will be calculuated into two lists
<br>
i.e., Sum of rows: [2,3,5]; Sum of Columns: [1,7,11]
<br>
-the largst number of the sums floor divided by 2 will be used in your scoring
<br>
i.e., 11 // 2 = 5 will be used in your scoring
<br>

# Scoring: Points are added on when you and subtracted when you lose.
<br>
i.e., if you lose: -5 points | if you win: +5 points
<br>
-Score will cumulate throughout games.
<br>
i.e., if you choose to play 3 games then your score will be changed 3 times and reset to 0 after.
<br>
Note: typing "-1" as your row number will immediately end the current game and calculuate the score based on the current board.
<br>

# Game Modes
<br>
-Solo: Play by yourself!
<br> 
-AI
<br>
* AI will randomly change a digit on the board to a random number on each turn after each of you moves.
<br>
Note: Max # of turns in AI mode is extended to (# of Rows x # of Columns) -1
<br>
i.e., on a 4x4 board the max # of turns per game would be (4x4)-1 = 16-1 = 15 turns
<br>

-Image Generation: An image will generate 
<br>

When a game ends your:
<br>
-Sum of Rows list will be converted into a horizontal image consisting of a colored blocks of x pixels wide/tall (determined by user) seperated by a black block of 10 pixels wide/tall.
<br> 
-Sum of Columns list will be converted into a vertical image consisting of a colored blocks of x pixels wide/tall (determined by user) seperated by a black block of 10 pixels wide/tall.
<br>
* Each number in the list corrsponds to a colour.
<br>
i.e., Sum of rows: [2,3,5]; Sum of Columns: [1,7,11]
<br>
2 corresponds to blue, 3 to red, 5 to brown etc.
<br>
i.e., for sum of rows expect a blue, red, brown block with a black block seperating each of them. 



