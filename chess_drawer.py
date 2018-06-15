## DAVID HOLCER
## ChessLine v1
## 5/28/18

'''
This code will draw a chess board and lines of moves from a pgn file (using Pygame)
'''

import itertools #to loop over colours
from math import * #import math functions
import pygame as pg #import pygame
from allFunctions import * #import all custom made functions
from time import sleep

pg.init() #initialize pg

#different modes
#black, regular, green
mode="regular"
# Set up the colors.
#WHITE=hsv2rgb(1,0, 1),
#WHITE=(255,255,255,0.5)
#LWHITE=(255,255,255)
LBLACK=(0, 0,0)
if mode=="regular" or mode=="white":
    LWHITE=(255,255,255)
    BWHITE=(236, 206, 168)
    BBLACK = (61, 34, 18)
elif mode=="black":
    LBLACK=(0,0,0)
    LWHITE=(255,255,255)
    BWHITE=(236, 206, 168)
    BBLACK = (61, 34, 18)
elif mode=="green":
    LWHITE=(236, 206, 168)
    BWHITE=(255,255,255)
    BBLACK = (12, 64, 53)
BLACK= (0,0,0)

#board size
tile_size = 70
length=10*tile_size
width=10*tile_size

#filename
#turn this into a question
fnums=5
files=[]
for i in range (1,fnums+1):
    files.append("%s.pgn"%(i))
#filename='5.pgn'

time=0
flip=False
while time<fnums:
    if flip:
        time-=1
    flip=False
    #print(mode)
    #print("AS")

    #FOLLOWING CODE PARTLY MODIFIED FROM https://stackoverflow.com/questions/45945254/make-a-88-chessboard-in-pygame-with-python
    screen = pg.display.set_mode((length, width))
    clock = pg.time.Clock()

    #allows for iters. btw. 2 colours
    colors = itertools.cycle((BWHITE, BBLACK))

    #chessboard size x,y
    square_w, square_h = 8*tile_size, 8*tile_size
    background = pg.Surface((square_w, square_h))

    for y in range(0, square_h, tile_size):
        for x in range(0, square_w, tile_size):
            #make ind. rectangles looping over x and y
            rect = (x, y, tile_size, tile_size)
            #change colours and add rect to board
            pg.draw.rect(background, next(colors), rect)
        #change colour
        next(colors)

    pg.draw.rect(background,BBLACK,[0,0,square_w,square_h],5)



    movesArray=fileToPos(files[time],0)

    tmoves=ceil(len(movesArray)/2)
    #fluctuation of colour
    flux=0.25
    #evenly spaced out over moves
    spacer=flux/ tmoves
    #c_spacer=155/len(movesArray)
    #print (spacer)
    #movesArray=[[[0,0],[0,0]],[[0,0],[1,1]]]

    #makes new lines surface in order for opacity to work
    lines = pg.Surface((square_w, square_h))
    #makes grey then sets fill to grey then sets colorkey to grey.
    #This makes it so that the background initiates as transparent.
    grey=hsv2rgb(1,0,0.5)
    if (mode!="black" and mode!="white"):

        lines.fill(grey)
        lines.set_colorkey(grey)
        #sets opacity of lines.
        lines.set_alpha(200)
    elif mode=="white":
        lines.fill(grey)
        lines.set_alpha(255)
    elif mode=="black":
        lines.fill(grey)
        lines.set_alpha(255)


    #counter to loop over moves
    c=1
    #thickness
    thns=5
    t_spacer=thns/tmoves

    while c<len(movesArray):
        cmove=ceil(c/2)
        #pg.draw.line(background, BBLACK, (0,0),(20,20))
        coords=posToCoords(movesArray[c],tile_size)
        #pg.draw.line(background, BBLACK, (0,0),(20,20))
    #    print ((cmove*spacer))

        if (c%2):
            #hsv2rgb(1,0, (1-(cmove*spacer) ) )
            #.963888889,.11,.97
            #
        #    if mode !="black":
            pg.draw.line(lines, LWHITE , (coords[0][0],coords[0][1]),(coords[1][0],coords[1][1]),thns)
        #    else:
        #        pg.draw.line(lines, LBLACK , (coords[0][0],coords[0][1]),(coords[1][0],coords[1][1]),thns)
        else:
            #hsv2rgb(1,0, ((cmove*spacer)))
            #.536111111,1,.22
            #hsv2rgb(1,0, 0)
        #    if mode !="black":
            pg.draw.line(lines, LBLACK , (coords[0][0],coords[0][1]),(coords[1][0],coords[1][1]),thns)
        #    else:
        #        pg.draw.line(lines, LWHITE , (coords[0][0],coords[0][1]),(coords[1][0],coords[1][1]),thns)

        #sleep(0.1)
        c+=1


    #FINAL DRAWING

    #allows for quitting
    game_exit = False
    while not game_exit and not flip:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                    sys.exit()
                elif event.key==pg.K_RIGHT:
                    game_exit = True
                elif event.key==pg.K_b:
                    if mode=="black":
                        mode="white"
                    elif mode=="white":
                        mode="black"
                    flip=True


        #bg colour
        screen.fill((60, 70, 90))
        #blit=add to screen/bg. 2nd argument is displacement so that everything is centered
        screen.blit(background, ((length-square_w)/2, (length-square_h)/2))
        screen.blit(lines, ((length-square_w)/2, (length-square_h)/2))
        pg.display.flip()
        clock.tick(30)

        #game_exit=True

    #time+=1
    sleep(1)
    time+=1
    pg.quit()
