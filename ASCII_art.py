import numpy as np
import cv2
from string import printable
from random import choice

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def display(windowsTitle,img):
  cv2.imshow(windowsTitle, img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def randomASCIIChar():
  return choice(list(printable))

def toRGB(img,char=''):
  resized = cv2.resize(img, (80,30))              #change (80,30) to desired output dimensions (width, height)
  for i in resized :
    for j in i :
      if(char==''):
        print(colored(j[2],j[1],j[0], randomASCIIChar()), end="")
      else:
        print(colored(j[2],j[1],j[0], char), end="")
    print('')  


def toBlackAndWhite(img, char=''):
  resized = cv2.resize(img, (80,30))            #change (80,30) to desired output dimensions (width, height)
  grayImage = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
  thresh, blackWhiteImage = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
  for i in blackWhiteImage :
    for j in i:
      if(char==''):
        if(j == 0):
          print(colored(0,0,0,randomASCIIChar()),end="")
        elif(j==255):
          print(colored(255,255,255,randomASCIIChar()), end="")
      else:
        if(j == 0):
          print(colored(0,0,0,char),end="")
        elif(j==255):
          print(colored(255,255,255,char), end="")
    print('')


def toGray(img, char=''): 
  resized = cv2.resize(img, (80,30))            #change (80,30) to desired output dimensions (width, height)
  grayImage = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
  for i in grayImage :
    for j in i:
      if(char==''):
        print(colored(j,j,j,randomASCIIChar()),end="")
      else :
        print(colored(j,j,j,char),end="")
    print("")


def toBlackAndWhitespace(img, char=''):
  resized = cv2.resize(img, (80,30))            #change (80,30) to desired output dimensions (width, height)
  grayImage = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
  thresh, blackWhiteImage = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
  for i in blackWhiteImage :  
    for j in i:
      if(char=='' and j == 0):
        print(randomASCIIChar(),end="")
      elif(j == 0):
        print(char,end="")
      elif(j==255):
        print(" ", end="")
    print("")


def toWhiteAndWhitespace(img, char=''):
  resized = cv2.resize(img, (80,30))            #change (80,30) to desired output dimensions (width, height)
  grayImage = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
  thresh, blackWhiteImage = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
  for i in blackWhiteImage :  
    for j in i:
      if(char=='' and j == 255):
        print(randomASCIIChar(),end="")
      elif(char != '' and j == 255):
        print(char,end="")
      elif(j==0):
        print(" ", end="")
    print("")



img = cv2.imread("imagePath")      #change image path

##################
toWhiteAndWhitespace(img)      #change method here to "toRGB" or "toWhiteAndWhitespace" or "toBlackAndWhitespace" or "toGray" or "toBlackAndWhite"
                                   #change '#' to whatever charact you want your ASCII art to be based on, or remove it to get an ASCII art with random characts
##################

