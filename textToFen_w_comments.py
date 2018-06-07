import sys
sys.path.append("./pgnToFen-master")

a=['e4 d6 ', 'e4 d6 d4 Nf6 ', 'e4 d6 d4 Nf6 Nc3 g6 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 f3 b5 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 f3 b5 Nge2 Nbd7 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 f3 b5 Nge2 Nbd7 Bh6 Bxh6 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 f3 b5 Nge2 Nbd7 Bh6 Bxh6 Qxh6 Bb7 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 f3 b5 Nge2 Nbd7 Bh6 Bxh6 Qxh6 Bb7 a3 e5 ']


'''
import pgnToFen # assumes you have pgntofen.py in the same directory, or you know how to handle python modules.
pgnConverter = pgnToFen.PgnToFen()
pgnConverter.resetBoard()
PGNMoves ='e4 d4'
pgnConverter.pgnToFen(PGNMoves.split(' '))
fen = pgnConverter.getFullFen()
print (fen)

pgnConverter = pgnToFen.PgnToFen()
PGNMoves ='e4 d6 d4 Nf6 '
pgnConverter.pgnToFen(PGNMoves.split(' '))
fen = pgnConverter.getFullFen()
print (fen)

#fen will be 'rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b - KQkq'
'''

import pgnToFen # assumes you have pgntofen.py in the same directory, or you know how to handle python modules.
PGNMoves ='e4 d4'

def textToFen(PGNMoves):
    pgnConverter = pgnToFen.PgnToFen()
    pgnConverter.resetBoard()
    pgnConverter.pgnToFen(PGNMoves.split(' '))
    fen = pgnConverter.getFullFen()
    return fen

#    pgnConverter.pgnToFen(PGNMoves.split(' '))
 #   fen = pgnConverter.getFullFen()
#fen will be 'rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b - KQkq'

print (textToFen('e4 d6 '))
print (textToFen('e4 d6 d4 Nf6 '))

'''
a=['e4 d6 ', 'e4 d6 d4 Nf6 ', 'e4 d6 d4 Nf6 Nc3 g6 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 f3 b5 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 f3 b5 Nge2 Nbd7 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 f3 b5 Nge2 Nbd7 Bh6 Bxh6 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 f3 b5 Nge2 Nbd7 Bh6 Bxh6 Qxh6 Bb7 ', 'e4 d6 d4 Nf6 Nc3 g6 Be3 Bg7 Qd2 c6 f3 b5 Nge2 Nbd7 Bh6 Bxh6 Qxh6 Bb7 a3 e5 ']
#PGNMoves ='e4 d4'

pgnConverter = pgnToFen.PgnToFen()
print (pgnConverter)

def textToFen(PGNMoves):
    pgnConverter = pgnToFen.PgnToFen()
   # print (pgnConverter)
    pgnConverter.pgnToFen(PGNMoves.split(' '))
    fen = pgnConverter.getFullFen()
    return fen

print(textToFen('e4 d6'))
#pgnConverter = pgnToFen.PgnToFen()
print(textToFen('e4 d6 d4 Nf6'))

#fen will be 'rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b - KQkq'
#print (textToFen('e4 d6 d4 Nf6 '))
'''
