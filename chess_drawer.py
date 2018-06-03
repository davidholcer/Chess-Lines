## DAVID HOLCER
## ChessLine v1
## 5/28/18

'''
This code will draw a chess board an lines of moves from a pgn file
'''

import itertools
import pygame as pg


pg.init()

# Set up the colors.
WHITE = (255, 255, 255)
BLACK = (12, 64, 53)

#board size
length=600
width=600

'''
FOLLOWING CODE MODIFIED FROM https://stackoverflow.com/questions/45945254/make-a-88-chessboard-in-pygame-with-python
'''

screen = pg.display.set_mode((length, width))
clock = pg.time.Clock()

#allows for iters. btw. 2 colours
colors = itertools.cycle((WHITE, BLACK))
tile_size = 50
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

pg.draw.rect(background,BLACK,[0,0,square_w,square_h],5)









#FINAL DRAWING

#allows for quitting
game_exit = False
while not game_exit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_exit = True

    #bg colour
    screen.fill((60, 70, 90))
    #move bg so that everything is centered
    screen.blit(background, ((length-square_w)/2, (length-square_h)/2))

    pg.display.flip()
    clock.tick(30)

pg.quit()
