import random
mlist = []
shufflelist = []
mtable = ''
def mult_fn(i):
    j = 12
    mr = 1
    while j >= 1:
        mr = i * j
        #print(i)
        #print(j)
        #print(mr)
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
input = input('Enter Multiplication table to generate:')
i = int(input)
mult_fn(i)






