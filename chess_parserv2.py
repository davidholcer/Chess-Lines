import sys
sys.path.append("./pgnToFen-master")

import pgnToFen # assumes you have pgntofen.py in the same directory, or you know how to handle python modules.
pgnConverter = pgnToFen.PgnToFen()
PGNMoves ='e4 d4'
pgnConverter.pgnToFen(PGNMoves.split(' '))
fen = pgnConverter.getFullFen()
#fen will be 'rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b - KQkq'
print (fen)
