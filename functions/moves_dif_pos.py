from fenToArray import fenToArray
from textToFen import textToFen
from chess_parser import movesMade
import numpy as np

#filename='k.pgn'

def fileToPos (filename):
    moves=movesMade(filename)
    #start from empty moves, continually adds to moves
    totalmoves=''
    #gets starting array
    fen=textToFen(totalmoves)
    pArray=(fenToArray(fen))

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
#print(fileToPos(filename))
