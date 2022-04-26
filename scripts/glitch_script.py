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

def open_photomontage(image):
    '''
    Takes a filepath for the photo that is being opened.
    '''
    image = Image.open(image)
    return image.show()
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

    img = Image.open(r'/Users/rodrigoguerrero/Documents/GitHub/ista301final/images/test_image.JPG')
    
    glitch_img = glitcher.glitch_image(img, glitch_amount(), color_offset= color_offset(), seed = random_seed())

    glitch_img.save(r'/Users/rodrigoguerrero/Documents/GitHub/ista301final/output/test_out.jpg')

while True:
    x = (input("Press 'Enter' to glitch the photomontage "))
    if x == "":
        glitch_image()
        open_photomontage('/Users/rodrigoguerrero/Documents/GitHub/ista301final/output/test_out.jpg')
    else:
        print("Oops! It seems you pressed a key that I don't understand. Unfortunately, Rodrigo isn't the best programmer on the planet so, if this was a mistake, you will need to re-run me to create your glitch art. Sorry! But if you did mean to exit, well, fuck you.")
        break