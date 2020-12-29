#CMPT 120 D100
#Final Project: The Even Colorful Game
#Authors: Alex MacLeod and Johnson Luong
#Date: December 7th, 2020
#module with functions for the processing of the game

import random


def welcome():
    '''
    INPUT: N/A
    OUTPUT: prints initial messages to user
    '''
    
    print("Dear player, welcome to the 'Even Colorful' game!\n\n")

    print(
        "With this system you will be able to play as many games as you want!")
    print(
        "The objective of this game is that all columns and rows in the board add to an even number."
    )
    print("For each game: ")
    print(
        "- you will be able to choose to play 'solo' or against the computer ('AI')"
    )
    print("- you will be able to choose an initial board")
    print("- at the end of each game you will win (or lose) points, and")
    print(
        "- you will see a colorful representation of the final game board results"
    )

def create_initial_board(boardID):
    '''
    INPUT: boardID (1,2 or 3)
    -reads from a file boardX.csv,
    -where X is the BoardID
    OUTPUT: list of lists (2D array) representing
    game board
    '''
    file = open(boardID)
    
    #get rid of header
    file.readline()

    board_list = []
    for line in file:
        line_list = line.strip().split(",")
        
        #help with map() from https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
        line_list = list(map(int,line_list))
        board_list.append(line_list)
    return board_list


def create_board_table(board,title):
  '''
  INPUT: list of lists (2D array) representing game board, 
  title for game board
  OUTPUT: print title and print game board in neatly
  organized rows and columns 
  '''

  #print out title
  print("\nThe board is:")
  print("-------------\n")
  print(title,"\n")


  #prints out the column header
  print("", end = '\t')
  for x in range(len(board)-1):
    print("col\t" + str(x),end = '\t')
  print("col " + str(len(board)-1))

  i = 0
  for x in board:
    #prints out the row header
    print("row " + str(i), end = '\t')
    i += 1
    for y in x:
      print(y,end='\t\t')
    print()
  


def edit_board(board):
    '''
    INPUT: list of lists (2D array) representing 
    game board
    -ask user for board place to change
    -ask user for digit to insert
    OUTPUT: updated array according to user input
    '''

    continue_user_x = True
    while continue_user_x:
      user_x = input("Which row? (type -1 to skip rest of turns and end game): ").strip()

      if user_x.isdigit() or user_x == "-1":
        user_x = int(user_x)
        if user_x <= len(board)-1 and user_x >= 0:
          continue_user_x = False
        elif user_x == -1:
          return board,user_x
        else:
          print("Sorry, that row doesn't exist")
      else:
        print("Only integer values allowed, please re-enter")

    
    continue_user_y = True
    while continue_user_y:
      
      user_y = input("Which column?: ").strip()
      
      if user_y.isdigit():
        user_y = int(user_y)
        if user_y <= len(board[0])-1 and user_y >= 0:
          continue_user_y = False
        else:
          print("Sorry, that column doesn't exist")
      else:
        print("Only integer values allowed, please re-enter")

    continue_user_digit = True
    while continue_user_digit:
      
      user_digit = input("What digit? (0 to 9): ").strip()

      if user_digit.isdigit():
        user_digit = int(user_digit)
        if user_digit <= 9 and user_digit >= 0:
          continue_user_digit = False
        else:
          print("Value must be between 0 and 9")
      else:
        print("Only integer values allowed, please re-enter")

      board[user_x][user_y] = user_digit
    
    return board,user_x


def ai_turn(board):
  '''
  INPUT: list of lists (2D array) representing game board
  OUTPUT: updated array with random value changed
  '''

  ai_x = random.randint(0,len(board)-1)
  ai_y = random.randint(0,len(board[0])-1)
  print(ai_y,ai_x)
  ai_digit = random.randint(0,9)

  board[ai_x][ai_y] = ai_digit
  return board,ai_x,ai_y


def calc_sumcols(board):
    '''
    INPUT: list of lists (2D array) representing game board
    OUTPUT: list with the numbers resulting from adding numbers in all the columns.
    '''
    col_totals = []
    
    for col in range(len(board)):
      col_sum = 0
      for row in range(len(board)):
        col_value = board[row][col]
        col_sum += col_value
      col_totals.append(col_sum)
    
    return col_totals


def calc_sumrows(board):
    '''
    INPUT: list of lists (2D array) representing game board
    OUTPUT: list with the numbers resulting from adding numbers in all the rows.
    '''
    row_totals = []

    for row in board:
      row_sum = 0
      for item in row:
        row_sum += item
      row_totals.append(row_sum)
    return row_totals


def check_even(lst):
  '''
  INPUT: list containing integer values 
  OUTPUT: Boolean value for whether all values in list
  are even
  '''
  isEven = True
  
  for i in lst:
    if i % 2 != 0:
      isEven = False
  
  return isEven


def calc_points(final_row,final_col,turns,turns_left):
  '''
  INPUT: list of final row totals, list of final column
  totals, number of turns taken
  -find max of final row and column together
  -integer div by number of turns to get points
  OUTPUT: points and max value of both lists together
  '''

  max_final = max(final_row + final_col)
  if turns > 0:
    points = max_final/(turns-turns_left)
    points = round(points)
  else:
    points = max_final

  return points,max_final




