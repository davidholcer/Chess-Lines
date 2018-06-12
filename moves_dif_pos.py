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
total = np.empty( len(moves) )
print(total)

i=0
while i<len(moves):
    #adds to moves
    totalmoves+=(moves[i].split(' ')[0]+' ')
    print (totalmoves)
    #gets new array
    fen=textToFen(totalmoves)
    print (fen)
    #set current array
    cArray=(fenToArray(fen))
    #find dif between arrays
    dif=np.subtract(cArray,pArray)
    #set previous array
    pArray=cArray
    print(totalmoves)
    print (dif)
    #find unique nums
    nums=np.unique(dif)
    #find 0 to remove it
    index=np.where(nums==0)
    nums=(np.delete(nums,index))
    print (nums)
    #if nums.size>1 (i.e. =2 or =4) then either take 2 or take first 2.
    if nums.size>1:
        #print(nums[0])
        #find positions of 1st and 2nd nums
        pos1=np.asarray(np.where(dif==nums[0])).T
        pos2=np.asarray(np.where(dif==nums[1])).T
        #print(pos1,pos2)
        #join both pos arrays
        posT=np.append ( pos1, pos2 , axis=0)
        #print w/ current turn.
    #    posT=([i,posT])
        #total[i]=posT
        print (posT)
    else:
        posT=np.asarray(np.where(dif==nums[0])).T
    #    posT=([i,posT])
    #    total.append(total, posT)
        print (posT)
    try:
        totalmoves+=(moves[i].split(' ')[1]+' ')
        fen=textToFen(totalmoves)
        print (fen)
        cArray=(fenToArray(fen))
        dif=np.subtract(cArray,pArray)
        pArray=cArray
        print(totalmoves)
        print (dif)
        nums=np.unique(dif)
        index=np.where(nums==0)
        nums=(np.delete(nums,index))
        print (nums)

        if nums.size>1:
            #print(nums[0])
            pos1=np.asarray(np.where(dif==nums[0])).T
            pos2=np.asarray(np.where(dif==nums[1])).T
            #print(pos1,pos2)
            posT=np.append ( pos1, pos2 , axis=0)
    #        posT=([i,posT])
        #    total.append(tota, posT)
            print (posT)
        else:
            posT=np.asarray(np.where(dif==nums[0])).T
        #    posT=([i,posT])
        #    total.append(tota, posT)
            print (posT)


    except IndexError:
        pass

    i+=1
