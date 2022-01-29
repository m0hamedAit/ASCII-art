import numpy as np
import cv2

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def display(windowsTitle,img):
  cv2.imshow(windowsTitle, img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


def toRGB(img,char):
  resized = cv2.resize(img, (80,30))
  for i in resized :
    for j in i :
      print(colored(j[2],j[1],j[0], char), end="")
    print('')  


def toBlackAndWhite(img, char):
  resized = cv2.resize(img, (100,30))
  grayImage = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
  thresh, blackWhiteImage = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
  for i in blackWhiteImage :
    for j in i:
      if(j == 0):
         print(colored(0,0,0,char),end="")
      elif(j==255):
          print(colored(255,255,255,char), end="")
    print('')


def toGray(img, char):
  resized = cv2.resize(img, (100,70))
  grayImage = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
  for i in grayImage :
    for j in i:
      print(colored(j,j,j,char),end="")
    print("")


def toBlackAndWhitespace(img, char):
  resized = cv2.resize(img, (150,50))
  grayImage = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
  thresh, blackWhiteImage = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
  for i in blackWhiteImage :  
    for j in i:
      if(j == 0):
        print(char,end="")
      elif(j==255):
        print(" ", end="")
    print("")


def toWhiteAndWhitespace(img, char):
  resized = cv2.resize(img, (120,50))
  grayImage = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
  thresh, blackWhiteImage = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
  for i in blackWhiteImage :  
    for j in i:
      if(j == 255):
        print(char,end="")
      elif(j==0):
        print(" ", end="")
    print("")



img = cv2.imread("./images/xo.png")

toWhiteAndWhitespace(img,"#")
# display("t",img)

