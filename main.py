#CMPT 120 D100
#Final Project: The Even Colorful Game
#Authors: Alex MacLeod and Johnson Luong
#Date: December 7th, 2020
#main driver file with user dialogue
#note: to keep our code clean we have chosen to keep 
#the functions that process the game in a separate module 
#that can be found in gameFunctions.py

#import modules
import gameFunctions as g

import createBoardImages as cbi

import cmpt120imageWeek9 as img

#initialize counters and welcome user
user_points = 0

user_wins = 0

ai_wins = 0

game_num = 0

g.welcome()


continue_playing = True

#begin while loop that executes game
while continue_playing:

  user_play = input("\nWould you like to play (y/n): ").lower().strip()

  #get user input to select board and display
  if user_play == "y": 

    game_num += 1

    print("\nGame ",game_num)
    print("=========")

    #process to select initial board
    continue_board = True
    while continue_board:
      user_board = input("\nWhich initial board do you want to use? (1/2/3): ").strip()

      if user_board in ["1","2","3"]:
        user_board = "board"+ user_board + ".csv"
        continue_board = False
      else:
        print("Sorry, please choose 1, 2, or 3")

    initial_board = g.create_initial_board(user_board)

    g.create_board_table(initial_board,"(initial board)")

    
    #user chooses game type, which results in different runs of the game with different rules
    continue_type = True
    while continue_type:
      user_type = input("Which level do you want to play ('solo' or 'AI'): ").lower().strip()

      if user_type in ["solo","ai"]:
        continue_type = False
      else:
        print("Please choose 'solo' or 'ai'")

    #solo version of game starts here
    if user_type == "solo":

      max_turns = len(initial_board)-1
      
      #validation to ensure valid number of turns based on solo mode rules
      invalid_turns = True
      while invalid_turns:

        user_turns = input("How many turns would you like to play? The max is " + str(max_turns)+": ").strip()

        if user_turns.isdigit():
          user_turns = int(user_turns)
          if user_turns <= max_turns:
            invalid_turns = False
          else:
            print("Sorry, invalid number of turns")
        else:
          print("Only integer values allowed, please re-enter")

      #repeats game steps for selected number of turns
      skip_turns = False
      turn_counter = user_turns
      while turn_counter > 0 and skip_turns == False:
      
        edited_board = g.edit_board(initial_board)
        user_row = edited_board[1]

        if user_row == -1:
          skip_turns = True
        else:
          turn_counter -= 1
          initial_board = edited_board[0]
          g.create_board_table(initial_board,"(after user turn)")

        if user_turns != 0 and turn_counter==0:
          print("\nYou have reached the maximum number of turns, the game is over!")

    #ai version of game starts here
    else:

      max_turns = (len(initial_board) * len(initial_board[0]))-1

      #validation to ensure valid number of turns based on ai mode rules
      invalid_turns = True
      while invalid_turns:

        user_turns = input("How many turns would you like to play? The max is " + str(max_turns)+": ").strip()

        if user_turns.isdigit():
          user_turns = int(user_turns)
          if user_turns <= max_turns:
            invalid_turns = False
          else:
            print("Sorry, invalid number of turns")
        else:
          print("Only integer values allowed, please re-enter")
          
      #repeats game steps for selected number of turns
      skip_turns = False
      turn_counter = user_turns
      
      while turn_counter > 0 and skip_turns == False:
        
        edited_board = g.edit_board(initial_board)
        user_row = edited_board[1]

        if user_row == -1:
          skip_turns = True
        else:
          turn_counter -= 1
          initial_board = edited_board[0]
          g.create_board_table(initial_board,"(after user turn)")

          continue_game = input("\nNow the computer will play!\nPress return to continue ")

          ai_board = g.ai_turn(initial_board)
          initial_board = ai_board[0]

          ai_messg = "(after computer played ROW " +str(ai_board[1]) + " and COLUMN " + str(ai_board[2]) + ")"

          g.create_board_table(initial_board, ai_messg)
      
      if user_turns != 0:
          print("\nYou have reached the maximum number of turns, the game is over!")
     
    
    if user_turns == 0:
      print("\nI see that you have decided not to change the board!")
    
    #gameplay ends here, starts totalling scores
    row_totals = g.calc_sumrows(initial_board)
    col_totals = g.calc_sumcols(initial_board)

    even_rows = g.check_even(row_totals)
    even_cols = g.check_even(col_totals)

    points_max = g.calc_points(row_totals,col_totals,user_turns,turn_counter)
    
    #starts displaying game stats to user
    print("\nTotals for this game")
    print("----------------------")

    print("\nrow totals:", row_totals)
    print("\ncolumn totals:", col_totals)

    print("\nThe points resulting from this round are: ",points_max[0])

    print("\nThe points were calculated as: ")
    print("\nThe max of all numbers in final line and column (",points_max[1],")")
    print("Divided by the number of turns played (", user_turns-turn_counter,")")

    # adds or subtracts points and assigns win
    if even_cols == True or even_rows == True:
      print("\nYou Win!")
      print("\nAll numbers in the final line and column are even!")
      print("You will have ",points_max[0]," points added to your total")
      user_wins += 1
      user_points += points_max[0]
      
    else:
      print("\nYou Lose!")
      print("\nNot all sums in the final line and column are even!")
      print("\nYou will have ",points_max[0]," points subtracted from your total")

      ai_wins += 1
      user_points -= points_max[0]

    print("\nYou now have ",user_points," points")
    
    #process for displaying end of game images
    print("\nIn preparation for the images for the final line and column...")
      
    continue_pixels = True
    while continue_pixels:
      
      user_pixels =  input("How many pixels would you like per square? (recommend between 60 and 100): ")
      user_pixels = user_pixels.strip()

      if user_pixels.isdigit():
        user_pixels = int(user_pixels)
        continue_pixels = False
      else:
        print("Please enter an integer value")


    #create image for row colors and display
    show_row = input("Hit return to continue")

    row_color_list = cbi.create_rgb(row_totals,"colorcoding.csv")

    row_img = []
    for rgb in row_color_list:
      cbi.create_color_square(rgb,user_pixels,row_img)
    
    #showImage not working, using saveImage instead
    img.saveImage(row_img,"final_row.jpg")

      
    #create image for column colors and display 
    show_col = input("Hit return to continue")
      
    col_color_list = cbi.create_rgb(col_totals,"colorcoding.csv")
      
    col_img = []
    for rgb in col_color_list:
      cbi.create_color_square(rgb,user_pixels,col_img)
      
    col_final = cbi.create_transpose_img(col_img)

    #showImage not working, using saveImage instead
    img.saveImage(col_final,"final_col.jpg")
        

  elif user_play == "n":
    print("\nHope you enjoyed the Even Colorful Game!")

    print("\nTOTALS FOR ALL GAMES")
    print("Total user points: ",user_points)
    print("Total games user won: ",user_wins)
    print("Total games computer won: ",ai_wins)
    continue_playing = False

  else:
    print("Sorry, I don't understand ",user_play)
    