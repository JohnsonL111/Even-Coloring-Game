# cmpt120image.py
# Author: SFU CMPT 120
# Contains helper functions to wrap the
# pygame image functions

# import the necessary package which has modules
# for image processing
import pygame
import numpy

def getImage(filename):
  """
  Input parameter: filename - string containing image filename
                              to open (including .jpg)
  Returns: 3D array, i.e. 2D array of 3-element RGB list
           (list of list of RGB list )
          ex: [ [[0,0,0], [100,200,0]] , [[0,0,0], [100,200,0]] ]
  """
  image = pygame.image.load(filename)
  return pygame.surfarray.array3d(image).tolist()

def saveImage(pixels, filename):
  """
  Input parameters:
        pixels - 3d array,i.e. 2d array of RGB values (list)
        filename - string containing filename to save image
                   (including .jpg)
  Output: Saves a file with name filename, containing pixels
  """
  nparray = numpy.asarray(pixels)
  surf = pygame.surfarray.make_surface(nparray)
  (width, height, colours) = nparray.shape
  surf = pygame.display.set_mode((width, height))
  pygame.surfarray.blit_array(surf, nparray)
  pygame.image.save(surf, filename)

def showImage(pixels,title):
  """
  Input parameter:  pixels - 2d array of RGB values
                    title
  Output: show the image in a window
  """
  nparray = numpy.asarray(pixels)
  surf = pygame.surfarray.make_surface(nparray)
  (width, height, colours) = nparray.shape
  #width = int(width/2)
  #height = int(height/2)
  pygame.display.init()
  pygame.display.set_caption(title)  ### using title
  screen = pygame.display.set_mode()
  screen.fill((225, 225, 225))
  screen.blit(surf, (0, 0))
  pygame.display.update()

def createBlackImage(width, height):
  result = numpy.zeros((width, height, 3)).tolist()
  return result