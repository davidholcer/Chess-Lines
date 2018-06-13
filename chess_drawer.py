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

pg.init() #initialize pg

#filename
#turn this into a question
filename='2.pgn'

# Set up the colors.
#WHITE=hsv2rgb(1,0, 1),
WHITE=(255,255,255,0.5)
LWHITE=(255,255,255)
LBLACK=(0, 0,0)
BWHITE=(236, 206, 168)
BBLACK = (61, 34, 18)
BLACK= (0,0,0)

#board size
tile_size = 70
length=10*tile_size
width=10*tile_size


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



movesArray=fileToPos(filename)

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
lines.fill(grey)
lines.set_colorkey(grey)
#sets opacity of lines.
lines.set_alpha(200)

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
        pg.draw.line(lines, hsv2rgb(1,0,1) , (coords[0][0],coords[0][1]),(coords[1][0],coords[1][1]),thns)
    else:
        #hsv2rgb(1,0, ((cmove*spacer)))
        #.536111111,1,.22
        pg.draw.line(lines, hsv2rgb(1,0, 0) , (coords[0][0],coords[0][1]),(coords[1][0],coords[1][1]),thns)

    #sleep(0.1)
    c+=1


#FINAL DRAWING

#allows for quitting
game_exit = False
while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True

    #bg colour
    screen.fill((60, 70, 90))
    #blit=add to screen/bg. 2nd argument is displacement so that everything is centered
    screen.blit(background, ((length-square_w)/2, (length-square_h)/2))
    screen.blit(lines, ((length-square_w)/2, (length-square_h)/2))
    pg.display.flip()
    clock.tick(30)

pg.quit()
