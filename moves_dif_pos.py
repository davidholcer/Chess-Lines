from fenToArray import fenToArray
from textToFen import textToFen
from chess_parser import movesMade
import numpy as np

filename='k.pgn'

moves=movesMade(filename)
#print (moves)
#start from empty moves, continually adds to moves
totalmoves=''
#gets starting array
fen=textToFen(totalmoves)
pArray=(fenToArray(fen))
#print (fen, pArray)

i=0
while i<len(moves):
    #adds to moves
    totalmoves+=(moves[i].split(' ')[0]+' ')
    print (totalmoves)
    #gets new array
    fen=textToFen(totalmoves)
    cArray=(fenToArray(fen))
    dif=np.subtract(cArray,pArray)
    print(dif)
    #print(dif)
    pArray=cArray

    try:
        totalmoves+=(moves[i].split(' ')[1]+' ')
        fen=textToFen(totalmoves)
        cArray=(fenToArray(fen))
        dif=np.subtract(cArray,pArray)
        pArray=cArray
        print(totalmoves)
        print (dif)
    except IndexError:
        pass

    i+=1

#    dif=

#    i+=1
#print (tmoves)
