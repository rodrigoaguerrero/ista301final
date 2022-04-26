'''
enter 'source glitch_env/bin/activate' to terminal to enter virtual environment
then naviate to directory

'''
from json import load
from PIL import Image
from glitch_this import ImageGlitcher
import random
import time
import sys
import os

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

def intro():

    exitmessage = "Oops! It seems you pressed a key other than 'Enter'. Unfortunately, Rodrigo isn't the best programmer on the planet so, if this was a mistake, you will need to re-run the script to create your glitch art. Sorry! But if you did mean to exit, well, fuck you."
    message1 = "Hello! (Press enter to continue, not only here but throughout the rest of our time together.)\n "
    message2 = "Our names are Rodrigo Guerrero and Sylvia Zarnescu.\n"
    message3 = "What you are about to experience is the opportunity to create some glitch art.\n"
    message4 = "However, what makes this glitch art unique is two fold:\n"
    message5 = "1. The art that you will be glitching is a photomontage created by the both of us and represents the both of us.\n"
    message6 = "It represents not only the both of us as individuals but the friendship we have created since we first met, nearly 10 years ago, in the fall of 2013.\n "
    message7 = "That sure was a long time ago. How long you might ask? Well, the song on the top of the Hot 100 that year? 'Thrift Shop' by Macklemore and Ryan Lewis."

    for char in message1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
        
    take_input1 = input()

    if take_input1 == "":

        for char in message2:

            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
            take_input2 = input()

            if take_input2 == "":

                for char in message3:

                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)

            else:
                
                for char in exitmessage:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)
                    time.sleep(5)

    else:
        for char in exitmessage:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(5)



def main():
    load_animation()
    intro()
    #
    #intro()
    '''
    random.seed(random.randint(1,2000000))
    x = random.random()
    print(x)

    glitcher = ImageGlitcher()

    img = Image.open(r'/Users/rodrigoguerrero/Documents/GitHub/ista301final/images/test_image.JPG')
    print(img

    glitch_img = glitcher.glitch_image(img, 8, color_offset=True, seed = x)

    glitch_img.save(r'/Users/rodrigoguerrero/Documents/GitHub/ista301final/output/test_out.jpg')
    '''
    
if __name__ == "__main__":
    main()