# Even-Coloring-Game 

# CMPT 120 Intro to CS I Final Project 😫
Play it here! ----> https://repl.it/@CMPT120Game/EvenColoringGame

# How-to-Play: 

<br> 
<ol>
<li> Select one of the three starter boards (displayed as a square matrix). C = Column and R = Row.
<br><br>
 <b> Game Board 3: </b>
<br>
 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;           C2 <br> 
&nbsp;&nbsp;&nbsp;&nbsp;R0&nbsp; 0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2 <br>
&nbsp;&nbsp;&nbsp;&nbsp;R1&nbsp; 1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4 <br>
&nbsp;&nbsp;&nbsp;&nbsp;R2&nbsp; 0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 <br> 
</li>
<li> Select num. of games you want to play </li> 
<br>
<li> Select # of turns (max num. of turns is: num. of rows - 1) eg. 4 row board = 3 turns max </li>
<br>
<li> The user can change 1 digit on the board to any # between 0-9. </li>
<br>
<li> Game ends when all turns are used. </li>
<br>
 </ol> 
<b> Objective: Make all rows and columns add up to an even number. </b> 
<br> 

# Point Calculuation: 
<br>
<ul>
 <li> The sum of each row and column will be calculuated into two lists </li>
<br>
 <li><b> i.e., Sum of rows: [2,3,5]; Sum of Columns: [1,7,11] </b> </li> 
<br>
 <li> the largst number of the sums floor divided by 2 will be used in your scoring. </li> 
<br>
 <li><b> i.e., 11 // 2 = 5 will be used in your scoring </b> </li>
</ul>
<br>

# Scoring
<br>
<ul>
 <li>  Points are added on when you win and subtracted when you lose. </li>
 <li> i.e., if you lose: -5 points | if you win: +5 points </li> 
<br>
 <li> Score will cumulate throughout games. </li>
<br>
<li> i.e., if you choose to play 3 games then your score will be changed 3 times and reset to 0 after. </li>
<br>
<li> Note: typing "-1" as your row number will immediately end the current game and calculuate the score based on the current board. </li> 
</ul> 
<br>

# Game Modes
<br>
<b> Solo: </b>
<ul>
 <li> Play by yourself! </li>
</ul>
<br> 
<b> AI </b>
<ul>
 <li> AI will randomly change a digit on the board to a random number on turn after each of you moves. </li>
 <li> Note: Max # of turns in AI mode is extended to (# of Rows x # of Columns) -1 </li>
 <li>i.e., on a 4x4 board the max # of turns per game would be (4x4)-1 = 16-1 = 15 turns </li>
</ul>
<br><br>


# Image Generation
<br>

<b> When a game ends your: </b>
<br>
<ul>
<li> Sum of Rows list will be converted into a horizontal image consisting of a colored blocks of x pixels wide/tall (determined by user) seperated by a black block of 10 pixels wide/tall. </li>
<br> 
<li> Sum of Columns list will be converted into a vertical image consisting of a colored blocks of x pixels wide/tall (determined by user) seperated by a black block of 10 pixels wide/tall. </li>
<br>
<ul>
 <li> Each number in the list corrsponds to a colour. </li>
<br>
 <li> i.e., Sum of rows: [2,3,5]; Sum of Columns: [1,7,11] </li>
<br>
 <li> 2 corresponds to blue, 3 to red, 5 to brown etc. </li>
<br>
<li> i.e., for sum of rows expect a blue, red, brown block with a black block seperating each of them. </li>



