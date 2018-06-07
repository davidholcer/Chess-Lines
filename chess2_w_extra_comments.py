import numpy as np
from io import StringIO

'''
a = np.array([[1,2,3], [4,5,6]])
b=np.reshape(a, (3,-1)) 
print(b)
'''
#fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR".split('/')

fen='rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b - KQkq'

# want
'''board=[[10,9,8,11,12,8,9,10],
       [7,7,7,7,7,7,7,7],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,1],
       [4,3,2,5,6,2,3,4]]


c = StringIO("1,0,2 \n 3,0,4")
y = np.loadtxt(c, delimiter=',', unpack=True)
print (y)  
'''

def fenArray(fen):
    fen=fen.split(' ')[0].split('/')
    pieces={'r':'10','n':'9','b':'8','q':'11','k':'12','p':'7','R':'4','N':'3','B':'2','Q':'5','K':'6','P':'1'}
    #loops over fen rows adding to final board string.
    board=''
    for row in fen:
      crow=''
      for piece in row:
        if piece.isdigit():
          crow+=('0, '*int(piece))
        else:
          crow+=(pieces.get(piece)+', ')
      board+=(crow[:-2]+'\n ')
    board=board[:-2]
    print (board)
    c=StringIO(board)
    bArray=np.loadtxt(c, delimiter=',')#,unpack=True)
    return (bArray)

print (fenArray(fen))

#np.fromstring('1 2', dtype=int, sep=' ')
