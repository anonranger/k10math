import random
shufflelist = []

def mult_fn(i):
    j = 12
    mlist=[]
    while j >= 1:
        #Worksheet hide result
        mtable = str(i)+" "+"*"+" "+str(j)+" "+"="+" "
        mlist.append(mtable)
        j = j - 1
    # print list as map - vertically [Sequential list]
    print('\n')
    print ("Multiplication Table:"+" "+str(i)+" "+"[Sequential list]")
    print('\n'.join(map(str, mlist)))
    from random import shuffle
    shufflelist = mlist[:]
    shuffle(shufflelist)
    #print(shufflelist)
    # print list as map - vertically [Shuffled List]
    print('\n')
    print ("Multiplication Table:"+" "+str(i)+" "+"[Shuffled List]")
    print('\n'.join(map(str, shufflelist)))

repeats = int(input())
for j in range(repeats):
    for i in range(2,13):
        mult_fn(i)
