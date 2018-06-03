import pgn
import sys

f = open('k.pgn')
pgn_text = f.read()
f.close()
games = pgn.loads(pgn_text)
#moves= pgn._parse_moves(pgn_text)
for game in games:
    print (game.moves)
