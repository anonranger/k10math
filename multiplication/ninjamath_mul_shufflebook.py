import random
mlist = []
shufflelist = []
mtable = ''
repeat_12 = 10
j = 12


def mult_fn(i):

    #print(i)
    j = 12
    
    while j >= 1:
        
        #print(i)
        #print(j)
       
        #Worksheet hide result
        mtable = str(i)+" "+"*"+" "+str(j)+" "+"="+" "+" "
        mlist.append(mtable)
        j = j - 1
    print('\n')
    # print list as map - vertically [Sequential list]
    print ("Multiplication Table:"+" "+str(i)+" "+"[Sequential list]")
    print('\n')
    print('\n \n \n'.join(map(str, mlist)))
    from random import shuffle
    shufflelist = mlist[:]
    shuffle(shufflelist)
    #print(shufflelist)
    # print list as map - vertically [Shuffled List]
    print('\n')
    print ("Multiplication Table:"+" "+str(i)+" "+"[Shuffled List]")
    print('\n')
    print('\n \n \n'.join(map(str, shufflelist)))


#repeat_200 = 1
#while repeat_200 <= 2:
while repeat_12 <= 12:
    mult_fn(repeat_12)
    repeat_12 = repeat_12 + 1
    #print(repeat_12)
    #mult_fn(repeat_12)
    #repeat_12 = repeat_12 + 1
    #repeat_12 = 2
    #repeat_200 = repeat_200 + 1





