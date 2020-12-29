<Even-Coloring-Game>
Scuffed CMPT 120 Final Project 😫

<How-to-Play>
(1) Select 1 of the 3 starter boards (displayed as a square matrix)
 <br>&nbsp;&nbsp;&nbsp;&nbsp;C0    C1    C2 <br> 
R0 0&nbsp;3&nbsp;2 <br>
R1 1&nbsp;5&nbsp;4 <br>
R2 0&nbsp;0&nbsp;1 <br> 

Figure 1. Starter Board 3 (CX = Column X | RX = Row X)
(2) Select # of games you want to play
(3) Select # of turns (max # of turns is: # of rows - 1) eg. 4 row board = 3 turns max 
(4) The user can change 1 digit on the board to any # between 0-9.
(5) Game ends when all turns are used.


--- Objective: Make all rows and columns add up to an even number. ---


-Point Calculuation: 
(1) The sum of each row and column will be calculuated into two lists
i.e., Sum of rows: [2,3,5]; Sum of Columns: [1,7,11]
(2) the largst number of the sums floor divided by 2 will be used in your scoring
i.e., 11 // 2 = 5 will be used in your scoring

-Scoring: Points are added on when you and subtracted when you lose.
i.e., if you lose: -5 points | if you win: +5 points
(3) Score will cumulate throughout games.
i.e., if you choose to play 3 games then your score will be changed 3 times and reset to 0 after.
Note: typing "-1" as your row number will immediately end the current game and calculuate the score based on the current board.

-Game Modes
(1) Solo
* Play by yourself!
(2) AI
* AI will randomly change a digit on the board to a random number on each turn after each of you moves.
Note: Max # of turns in AI mode is extended to (# of Rows x # of Columns) -1 
i.e., on a 4x4 board the max # of turns per game would be (4x4)-1 = 16-1 = 15 turns 

-Image Generation: An image will generate 

When a game ends your:
(1) Sum of Rows list will be converted into a horizontal image consisting of a colored blocks of x pixels wide/tall (determined by user) seperated by a black block of 10 pixels wide/tall.
(2) Sum of Columns list will be converted into a vertical image consisting of a colored blocks of x pixels wide/tall (determined by user) seperated by a black block of 10 pixels wide/tall.
* Each number in the list corrsponds to a colour.
i.e., Sum of rows: [2,3,5]; Sum of Columns: [1,7,11]
2 corresponds to blue, 3 to red, 5 to brown etc.
i.e., for sum of rows expect a blue, red, brown block with a black block seperating each of them. 



