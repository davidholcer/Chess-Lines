from fenToArray import fenToArray
from textToFen import textToFen
from chess_parser import movesMade

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
while i<5:
    #adds to moves
    totalmoves+=(moves[i]+' ')
    print (totalmoves)
    #gets new array
    fen=textToFen(totalmoves)
    cArray=(fenToArray(fen))
    i+=1

#    dif=
    
#    i+=1
#print (tmoves)
