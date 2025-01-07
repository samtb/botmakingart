#!/usr/bin/env python

#twitter.com/botmakingart

import twitter
import os, sys
import random
import pygame
from pygame.locals import *
from PIL import Image
from PIL import ImageOps
from PIL import ImageFilter

# obviously, if you use this, do something better with your api credentials, this is just for illustrative purposes.
api = twitter.Api(consumer_key='YOURKEY', consumer_secret='YOURSECRET', access_token_key='YOUR-ACCESSTOKEN', access_token_secret='YOURACCESSTOKENSECRET')

a_perfect_piece_of_art = "a_perfect_ART.png"

outputImage = "ART.png"

blur = ImageFilter.GaussianBlur(2.0)
pygame.init()
# side_of_square = 700
side_of_square = 2000
APPLICATION_x_size = side_of_square
APPLICATION_y_size = side_of_square
screen = pygame.display.set_mode((APPLICATION_x_size, APPLICATION_y_size))
pygame.display.set_caption('Automatic drawing')
pygame.mouse.set_visible(True)
pygame.mouse.set_visible(False)
if random.randrange(1,3) == 2:
    square_that_is_the_size_of_the_screen = pygame.Surface(screen.get_size())
    square_that_is_the_size_of_the_screen.fill((255, 255, 255))
    screen.blit(square_that_is_the_size_of_the_screen, (0, 0))
pygame.display.flip()

blend_with_the_blur = [0,0,0.4,0.5,0.5,0.5,0.6,0.7,0.7,0.8,0.8,1,1]
is_running = True

if random.randrange(1,100) < 20:
    wildcolors = True
else:
    wildcolors = False

colorone = random.randrange(0,256)
colortwo = random.randrange(0,256)
if colorone > colortwo:
    colormin = colortwo
    colormax = colorone
else:
    colormin = colorone
    colormax = colortwo

colora1 = random.randrange(0,256)
colora2 = random.randrange(0,256)
if colora1 < colora2:
    coloramin = colora1
    coloramax = colora2
else:
    coloramin = colora2
    coloramax = colora1

colorb1 = random.randrange(0,256)
colorb2 = random.randrange(0,256)
if colorb1 < colorb2:
    colorbmin = colorb1
    colorbmax = colorb2
else:
    colorbmin = colorb2
    colorbmax = colorb1

colorc1 = random.randrange(0,256)
colorc2 = random.randrange(0,256)
if colorc1 < colorc2:
    colorcmin = colorc1
    colorcmax = colorc2
else:
    colorcmin = colorc2
    colorcmax = colorc1

if wildcolors:
        coloramin = 0
        colorbmin = 0
        colorcmin = 0
        coloramax = 255
        colorbmax = 255
        colorcmax = 255

def rand():
    # return random.choice([0,1,-1])
    return random.choice([0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20])

def fudgerand():
    return random.choice([0,1,-1])

def fudgeRandNonZero():
    return random.choice([1,-1])

def fudgeRandNonZeroBigger():
    return random.choice([1,2,3,4,5,-1,-2,-3,-4,-5])

def randpoint(point, side_of_square):
    randompoint = point + fudgerand()
    if randompoint > side_of_square:
        randompoint = side_of_square
    if randompoint < -side_of_square:
        randompoint = -side_of_square
    return randompoint

def randcolorbit(color):
    randomcolor = color + fudgerand()
    if randomcolor < colormin:
        randomcolor = colormin
    if randomcolor > colormax:
        randomcolor = colormax
    return randomcolor

def squiggleline(iterations):
    global coloramin
    global coloramax
    global colorbmin
    global colorbmax
    global colorcmin
    global colorcmax
    x = 200
    y = 200
    a = random.randrange(coloramin,coloramax+1)
    b = random.randrange(colorbmin,colorbmax+1)
    c = random.randrange(colorcmin,colorcmax+1)
    colorchange = random.randrange(1,4)
    for i in range(iterations):
        screen.set_at((x, y), (a, b, c))
        x = randpoint(x,side_of_square)
        y = randpoint(y,side_of_square)
        if colorchange == 1:        
            # a = randcolorbit(a)
            # b = randcolorbit(b)
            # c = randcolorbit(c)
            a = random.randrange(coloramin,coloramax)
            b = random.randrange(colorbmin,colorbmax)
            c = random.randrange(colorcmin,colorcmax)
        if colorchange in (2,3):
            a += fudgerand()
            b += fudgerand()
            c += fudgerand()
            if a < 0:
                a = 0
            if b < 0:
                b = 0
            if c < 0:
                c = 0
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
        # iterations = iterations - 1

def blobline(iterations):
    global coloramin
    global coloramax
    global colorbmin
    global colorbmax
    global colorcmin
    global colorcmax
    startx = 200
    starty = 200
    ex = startx
    ey = starty
    line_color = (random.randrange(coloramin,coloramax+1),random.randrange(colorbmin,colorbmax+1),random.randrange(colorcmin,colorcmax+1))
    # linewidth = 1
    linewidth = random.randrange(1,30)
    for i in range(iterations):
        linewidth = linewidth + random.choice([0,1,1,1,-1,-1,-1,-1])
        if linewidth < 1:
            linewidth = 1
        if linewidth > 40:
            linewidth = 40
        if ex > side_of_square:
            ex = side_of_square
        if ey > side_of_square:
            ey = side_of_square
        if ey < -side_of_square:
            ey = -side_of_square
        if ex < -side_of_square:
            ex = -side_of_square
        pygame.draw.line(screen,line_color,(startx,starty),(ex,ey),linewidth)
        starty = ey
        startx = ex
        ex = startx + rand()
        ey = starty + rand()

def checkforborder(number):
    fixed_number = number
    if number > side_of_square:
        fixed_number = side_of_square
    if number < -side_of_square:
        fixed_number = -side_of_square
    return fixed_number

def makestringline(iterations):
    global coloramin
    global coloramax
    global colorbmin
    global colorbmax
    global colorcmin
    global colorcmax
    list_of_points = []
    second_list_of_points = []
    for i in range(iterations):
        x = random.choice(range(side_of_square))
        x = checkforborder(x)
        y = random.choice(range(side_of_square))
        y = checkforborder(y)
        list_of_points.append((x,y))
        second_list_of_points.append((x+random.randrange(5,51),y+random.randrange(5,51)))
    line_color = (random.randrange(coloramin,coloramax+1),random.randrange(colorbmin,colorbmax+1),random.randrange(colorcmin,colorcmax+1))
    pygame.draw.aalines(screen, line_color, False, list_of_points,random.randrange(0,2))
    pygame.draw.aalines(screen, line_color, False, second_list_of_points,random.randrange(0,2))

def makesquare(iterations):
    global coloramin
    global coloramax
    global colorbmin
    global colorbmax
    global colorcmin
    global colorcmax
    for i in range(iterations):
        color = (random.randrange(coloramin,coloramax+1),random.randrange(colorbmin,colorbmax+1),random.randrange(colorcmin,colorcmax+1))
        Rect = (random.randrange(1,side_of_square),random.randrange(1,side_of_square),random.randrange(1,side_of_square),random.randrange(1,side_of_square))
        pygame.draw.rect(screen, color, Rect, 0)

def circlethings(iterations):
    global coloramin
    global coloramax
    global colorbmin
    global colorbmax
    global colorcmin
    global colorcmax
    positionx = random.randrange(0,side_of_square)
    positiony = random.randrange(0,side_of_square)
    radius = random.randrange(3,100)
    color = (random.randrange(coloramin,coloramax+1),random.randrange(colorbmin,colorbmax+1),random.randrange(colorcmin,colorcmax+1))
    for i in range(iterations):
        positionx += fudgerand()+fudgerand()
        positiony -= random.choice([0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-2,-3,-4,-5,-6])
        position = (positionx,positiony)
        radius += random.choice([0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,1,1,1,2,2])
        if radius < 1:
            return True
        pygame.draw.circle(screen,color, position, radius, 0)

def manypolygons(iterations):
    global coloramin
    global coloramax
    global colorbmin
    global colorbmax
    global colorcmin
    global colorcmax
    a = random.randrange(1,side_of_square)
    b = random.randrange(1,side_of_square)
    while a >= b:
        a = random.randrange(1,side_of_square)
        b = random.randrange(1,side_of_square)
    size = random.randrange(2,side_of_square/14)
    numsides = random.randrange(3,7)
    # numsides = 6
    for i in range(iterations):
        if random.randrange(1,11) < 2:
        # if random.randrange(1,11) > 0:
            twist = True
        else:
            twist = False
        if random.randrange(1,6) >= 5:
            a += random.randrange(-50,50)
            b += random.randrange(-50,50)
        else:
            a += fudgeRandNonZeroBigger()
            b += fudgeRandNonZeroBigger()
        size += fudgeRandNonZeroBigger()
        halfsize = size/2
        if size == 0:
            return True
        twistamount = random.randrange(5,100)
        if numsides == 3:
            if twist:
                list_of_points = [(a,b),(a-twistamount,b+twistamount),(a+twistamount,b+size+twistamount)]
            else:
                list_of_points = [(a,b),(a,b+size),(a+size,b)]
        if numsides == 4:
            if twist:
                list_of_points = [(a,b),(a-twistamount,b+size),(a+size,b+size+twistamount),(a+size+twistamount,b+twistamount)]
            else:
                list_of_points = [(a,b),(a,b+size),(a+size,b+size),(a+size,b)]
        if numsides == 5:
            if twist:
                list_of_points = [(a,b),(a-size+twistamount,b+twistamount),(a-size-halfsize-twistamount,b+size+twistamount),(a-halfsize-twistamount,b+size+twistamount),(a+halfsize+twistamount,b+halfsize)]
            else:
                list_of_points = [(a,b),(a-size,b),(a-size-halfsize,b+size),(a-halfsize,b+size),(a+halfsize,b+halfsize)]
        if numsides == 6:
            if twist:
                list_of_points = [(a,b),(a-size+twistamount,b+halfsize+twistamount),(a-size-twistamount,b+size+halfsize+twistamount),(a,b+size+size+twistamount),(a+size+twistamount,b+size+halfsize+twistamount),(a+size,b+halfsize+twistamount)]
            else:
                list_of_points = [(a,b),(a-size,b+halfsize),(a-size,b+size+halfsize),(a,b+size+size),(a+size,b+size+halfsize),(a+size,b+halfsize)]
        line_color = (random.randrange(coloramin,coloramax+1),random.randrange(colorbmin,colorbmax+1),random.randrange(colorcmin,colorcmax+1))
        pygame.draw.polygon(screen, line_color, list_of_points,random.randrange(1,3))

number_of_options = random.randrange(2,5)

for i in range(number_of_options):
    randomnumber = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
    # randomnumber = 26
    if randomnumber in (1,2,3,4):
        blobline(random.randrange(5000,50000))
    if randomnumber in (5,6,7,8,9,10):
        squiggleline(random.randrange(150000,800000))
    if randomnumber == 11:
        makestringline(random.randrange(800,30000))
    if randomnumber == 12:
        makesquare(random.randrange(1,20))
    if randomnumber in (13,14):
        circlethings(random.randrange(30,800))
    if randomnumber in (15,16,17,18,19):
        manypolygons(random.randrange(1,2000))

pygame.image.save(screen,outputImage)

while is_running:
    pygame.display.flip()
    # if the 'X' button is pressed the window should close:
    #pygame.image.save(screen,"mytest.png")
    is_running = False #comment this out to keep the image up when it is created
    Geesh = pygame.event.get()
    if len(Geesh) > 0:
        if Geesh[0].type == QUIT: is_running = False

## Once this line is reached the window should close

im = Image.open(outputImage)
# im = im.convert('L')
# im = im.filter(ImageFilter.SMOOTH_MORE)
# im = im.filter(ImageFilter.SMOOTH_MORE)
im = im.filter(ImageFilter.SMOOTH_MORE)
im = im.filter(ImageFilter.GaussianBlur(random.choice([5,10,10,20,20,20,30,30,40])))
# im = im.filter(ImageFilter.MedianFilter(size=3))
im.save("ARTblur.png")

image1 = Image.open(outputImage)
image2 = Image.open("ARTblur.png")
result = Image.blend(image1, image2, alpha=random.choice(blend_with_the_blur))
if random.randrange(1,11) == 1:
    result = result.convert('L')
result.save(a_perfect_piece_of_art)

with open(a_perfect_piece_of_art, "rb") as imagefile:
    imagedata = imagefile.read()

thetext = "ART"
status = api.PostUpdate(thetext,media=a_perfect_piece_of_art)
