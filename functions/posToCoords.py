import numpy as np

def posToCoords(c_array,tile_size):
    #[[5,5],[6,6]]
    total = np.array(  [ [0,0],[0,0]  ]  )
    #    print(total)

    total[0][0]=(c_array[0][1]+0.5)*tile_size
    total[0][1]=(c_array[0][0]+0.5)*tile_size
    total[1][0]=(c_array[1][1]+0.5)*tile_size
    total[1][1]=(c_array[1][0]+0.5)*tile_size
    return(total)

    '''
        a=0
        b=1
        while a<2:
            while b>-1:
                =
                b-=1
            b=1
            a+=1


            while b>-1:
                #total[1-a][1-b]=(c_array[a][b]+0.5)*tile_size
                b-=1
            b=1
            a+=1
            '''


#print(posToCoords([[1,2],[3,2]],50))

#0,1
#0,0
#1,1
#1,0
