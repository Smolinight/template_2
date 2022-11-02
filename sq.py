#!/usr/bin/python3

import turtle as tl
from random import randint
import random
from PIL import Image

def square():
    for i in range(4):
        tl.forward(100)
        tl.left(90)
def draw_square(n):
    for i in range(n):
        tl.begin_fill()
        colors = ['blue', 'yellow', 'green', 'pink', 'orange', 'grey', 'brown', 'red']
        tl.color(colors[randint(0, len(colors)-1)])
        square()
        if i != n-1:
            tl.goto(randint(-400, 400), randint(-400, 400))
        tl.end_fill()
tl.speed(5)
# n = int(input())
draw_square(5)
tl.goto(-100, 100)
tl.color('black')
tl.write("New commit new image!", font=("Times New Roman", 20, "normal"))
cv = tl.getcanvas()
cv.postscript(file="image.ps", colormode='color')
#tl.done()
psimage=Image.open('./image.ps')
psimage.save('./image.png')
