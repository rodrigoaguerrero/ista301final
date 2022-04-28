'''
enter 'source glitch_env/bin/activate' to terminal to enter virtual environment
then naviate to directory

'''
from asyncore import ExitNow
from json import load
import re
from turtle import color
from PIL import Image
from glitch_this import ImageGlitcher
import random
import time
import sys
import os

from numpy import take

def load_animation():
  
    # String to be displayed when the application is loading
    load_str = "starting your console application..."
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 100):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")
def type_writer(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(5)

def exit_module():
    print("Oops! It seems you pressed a key that I don't understand. Unfortunately, Rodrigo isn't the best programmer on the planet so, if this was a mistake, you will need to re-run me to create your glitch art. Sorry! But if you did mean to exit, well, fuck you.")
    time.sleep(5)
    exit()

def open_photomontage(image):
    image = Image.open(image)
    image.show()

def random_seed():
    random.seed(random.randint(1,200000))
    x = random.random()
    return x

def color_offset():
    options = [True, False]
    return random.choice(options)

def glitch_amount():
    return random.randint(1,10)

def glitch_image():

    glitcher = ImageGlitcher()

    img = Image.open(r'/Users/rodrigoguerrero/Documents/GitHub/ista301final/images/final.png')
    
    glitch_img = glitcher.glitch_image(img, glitch_amount(), color_offset= color_offset(), seed = random_seed())

    glitch_img.save(r'/Users/rodrigoguerrero/Documents/GitHub/ista301final/output/final_out.png')

def enter_loop():
    while True:
        x = input("Press the space bar, followed by 'enter' to glitch the photomontage ")
        if x == " ":
            glitch_image()
            print("The photomontage has been glitched!")
            open_photomontage('/Users/rodrigoguerrero/Documents/GitHub/ista301final/output/final_out.png')
        else:
            print("Oops! It seems you pressed a key that I don't understand. Unfortunately, Rodrigo isn't the best programmer on the planet so, if this was a mistake, you will need to re-run me to create your glitch art. Sorry! But if you did mean to exit, well, fuck you.")
            break
def intro():

    message1 = "Hello! (Press 'enter' to continue)\n "
    message2 = "Our names are Rodrigo Guerrero and Sylvia Zarnescu.\n"
    message3 = "What you are about to experience is the opportunity to participate in our final project and create art with us.\n"
    message4 = "What makes this art unique is as follows…\n"
    message5 = "For our final project, we have created a photomontage representing ourselves, our childhoods, and our futures. Naturally, graduating college is a scary concept with our futures uncertain and unknowable. We are currently sitting on perhaps the biggest margin of our lives, two living glitches in the system. You will get the chance to materialize that glitch over the next several minutes. \n"
    message6 = "This photomontage represents the friendship we have created and held since we first met, nearly 10 years ago, in the fall of 2013.\n "
    message7 = "That sure was a long time ago. How long you might ask? Well, the song on the top of the Hot 100 that year? 'Thrift Shop' by Macklemore and Ryan Lewis.\n"
    message8 = "But we digress... Now, let’s take a look at our original photomontage.\n"
    message9 = "Pretty cool, huh? Imagine this as an amalgamation of everything leading up to our college graduation. Now, let’s glitch it! You will now be asked to press the space bar. Each time you press the space bar, followed by the enter key you will be able to glitch the image randomly until it is at your liking. \n"
    
    type_writer(message1)
    take_input = input("")

    if take_input == "":
        type_writer(message2)
        take_input
        if take_input == "":
            type_writer(message3)
            take_input
            if take_input == "":
                type_writer(message4)
                take_input
                if take_input == "":
                    type_writer(message5)
                    take_input
                    if take_input == "":
                        type_writer(message6)
                        take_input
                        if take_input == "":
                            type_writer(message7)
                            take_input
                            if take_input == "":
                                type_writer(message8)
                                take_input
                                if take_input == "":
                                    open_photomontage("/Users/rodrigoguerrero/Documents/GitHub/ista301final/images/final.png")
                                    take_input
                                    if take_input == "":
                                        type_writer(message9)
                                        #ISSUE HAPPENS HERE
                                        enter_loop()
                                    else:
                                        exit_module()
                                else:
                                    exit_module()
                            else:
                                exit_module()
                        else:
                            exit_module()
                    else:
                        exit_module()
                else:
                    exit_module()
            else:
                exit_module()
        else:
            exit_module()
    else:
        exit_module()

def main():
   # load_animation()
    intro()
    #enter_loop()

if __name__ == "__main__":
    main()
