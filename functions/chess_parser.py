#this will get the moves from the .pgn file.
#from fenToArray import fenToArray
#from textToFen import textToFen

import sys
sys.path.append("./pgnToFen-master")
import pgnToFen

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
