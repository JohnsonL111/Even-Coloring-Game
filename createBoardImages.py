#CMPT 120 D100
#Final Project: The Even Colorful Game
#Authors: Alex MacLeod and Johnson Luong
#Date: December 7th, 2020
#module with functions for the creation of the color 
#display at the end of the game

import cmpt120imageWeek9 as img

def create_rgb(final_list,file):
    '''
    INPUT: List of final values for row OR column 
    -matches list values with color coding file
    OUTPUT: new list containing rgb values
    '''

    color_file = open(file)
    
    #stripping unneeded header
    color_file.readline()

    rgb_list = []
    
    for row_total in final_list:
      color_file.seek(0)
      for line in color_file:
        line_list = line.strip().split(",")

        if line_list[0] == str(row_total):
          rgb_list.append(line_list[1:4])

    #converting RGB elements to integers 
    rgb_list_int = []
    for lst in rgb_list:
      rgb_list = list(map(int,lst))
      rgb_list_int.append(rgb_list)

    return rgb_list_int
   


def create_color_square(rgb,size,res_img):
    '''
    INPUT: rgb values for a color as list, size per side
    in number of pixels, img list for colors values to be 
    appended to 
    OUTPUT: list with color square values appended into it
    '''
    
    blank_image = img.createBlackImage(size+10, size)
    
    for x in range(size):
      for y in range(size):
        blank_image[x][y] = rgb

    for i in blank_image:
      res_img.append(i)
    


def create_transpose_img(img):
    '''
    INPUT: image as 2D list of list of RGB pixels
    OUTPUT: transposed image (x and y swapped)
    '''

    #help with transpose from https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
    transposed = [[img[x][y] for x in range(len(img))] for y in range(len(img[0]))] 

    return transposed

    

