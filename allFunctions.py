#all functions used
#DAVID HOLCER
#6-13-18

'''
This file contains all functions used in order to map lines between chess moves made.
'''

import sys
sys.path.append("./pgnToFen-master") #localizes the library directory
import pgnToFen # assumes you have pgntofen.py in the same directory, or you know how to handle python modules.
import numpy as np #imports numpy module
from io import StringIO #used to make string into array


#this will get the moves from the .pgn file.
def movesMade(filename):
    #opens .pgn file
    lines = []                 # Declare an empty list named "lines"
    with open ('./pgn/%s'%filename, 'rt') as in_file:  # Open file lorem.txt for reading of text data.
        for line in in_file:  # For each line of text in in_file, where the data is named "line",
            lines.append(line.rstrip('\n'))   # add that line to our list of lines, stripping newlines.
    #gets the part after the newline
    moves=lines[(lines.index('')+1) :]
    #seperates moves by period after joining them as one array
    moves=' '.join(moves).split('. ')[1:]
    #loops over each move, taking only the first 2 moves and then joining them as one text.
    c=0
    while c<len(moves):
        moves[c]=moves[c].split(' ')[:-1]
        moves[c]=' '.join(moves[c])
        c+=1
    return (moves)


#converts text of moves to fen
def textToFen(PGNMoves):
    pgnConverter = pgnToFen.PgnToFen()
    #must reset board to continue getting moves
    pgnConverter.resetBoard()
    #has to split the moves since there is more than 2
    pgnConverter.pgnToFen(PGNMoves.split(' '))
    fen = pgnConverter.getFullFen()
    #fen will be smthing like 'rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b - KQkq'
    return (fen)


#converts fen text to piece array
def fenToArray(fen):
    #splits fen into rows
    fen=fen.split(' ')[0].split('/')
    #dictionary to map pieces to numbers
    pieces={'r':'10','n':'9','b':'8','q':'11','k':'12','p':'7','R':'4','N':'3','B':'2','Q':'5','K':'6','P':'1'}
    #loops over fen rows adding to final board string.
    board=''
    #loops over fen rows
    for row in fen:
      #current (number) row
      crow=''
      #loops over each piece in fen row
      for piece in row:
        #if piece is digit it is empty
        if piece.isdigit():
          crow+=('0, '*int(piece))
        #otherwise it is a piece so check the dictionary
        else:
          crow+=(pieces.get(piece)+', ')
      #adds the number row to the board (removing the last ', ')
      board+=(crow[:-2]+'\n ')
    #removes the last ', ' from the board
    board=board[:-2]
    #converts the string board to a numpy array.
    c=StringIO(board)
    bArray=np.loadtxt(c, delimiter=',')#,unpack=True)
    return (bArray)


#gets array and from that extracts the pos of the unique elements for all moves.
def fileToPos (filename):
    moves=movesMade(filename)
    #start from empty moves, continually adds to moves
    totalmoves=''
    #gets starting array
    fen=textToFen(totalmoves)
    #sets previous array at start
    pArray=(fenToArray(fen))
    #sets empty array at start (the 0 array is a placeholder and will be ignored)
    total = np.array(  [ [ [0,0],[0,0]  ] ] )

    i=0
    while i<len(moves):
        ##First part of move (the end might just have 1 move hence the try/except)
        #adds to moves
        totalmoves+=(moves[i].split(' ')[0]+' ')
        #gets new array
        fen=textToFen(totalmoves)
        #set current array
        cArray=(fenToArray(fen))
        #find dif between arrays
        dif=np.subtract(cArray,pArray)
        #set previous array
        pArray=cArray
        #find unique nums
        nums=np.unique(dif)
        #find 0 to remove it
        index=np.where(nums==0)
        nums=(np.delete(nums,index))
        #if nums.size>1 (i.e. =2 or =4) then either take 2 or take first 2.
        if nums.size>1:
            #find positions of 1st and 2nd nums
            pos1=np.asarray(np.where(dif==nums[0])).T
            pos2=np.asarray(np.where(dif==nums[1])).T
            #join both pos arrays
            posT=np.append ( pos1, pos2 , axis=0)
            total = np.append(total, [posT] ,0)
        else:
            posT=np.asarray(np.where(dif==nums[0])).T
            total = np.append(total, [posT] ,0)

        ##Second part of move (the end might just have 1 move hence the try/except)
        try:
            totalmoves+=(moves[i].split(' ')[1]+' ')
            fen=textToFen(totalmoves)
            cArray=(fenToArray(fen))
            dif=np.subtract(cArray,pArray)
            pArray=cArray
            nums=np.unique(dif)
            index=np.where(nums==0)
            nums=(np.delete(nums,index))
            if nums.size>1:
                pos1=np.asarray(np.where(dif==nums[0])).T
                pos2=np.asarray(np.where(dif==nums[1])).T
                posT=np.append ( pos1, pos2 , axis=0)
                total = np.append(total, [posT] ,0)
            else:
                posT=np.asarray(np.where(dif==nums[0])).T
                total = np.append(total, [posT] ,0)
        except IndexError:
            pass
        i+=1
    return(total)


#converts the pos into coordinates for the board
def posToCoords(c_array,tile_size):
    #empty array to which coords will go
    total = np.array(  [ [0,0],[0,0]  ]  )
    #converts pos (y,x) to coord (x,y)
    total[0][0]=(c_array[0][1]+0.5)*tile_size
    total[0][1]=(c_array[0][0]+0.5)*tile_size
    total[1][0]=(c_array[1][1]+0.5)*tile_size
    total[1][1]=(c_array[1][0]+0.5)*tile_size
    return(total)

#converts an hsb (hsv) value into an rgb one.
#source: https://stackoverflow.com/questions/24852345/hsv-to-rgb-color-conversion
import colorsys
def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
