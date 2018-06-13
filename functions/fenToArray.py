import numpy as np
from io import StringIO

#fen='rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b - KQkq'

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
