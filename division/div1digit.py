import random
from random import shuffle
shufflelist = []

def print1(j,k):
    print(str(j) + " " + "÷" + " " + str(k) + " " + "=" + " ")
    #print('\n')

def mult_fn(i):
    j = 12
    mlist=[]
    while j >= 1:
        mlist.append(i*j)
        j = j - 1
    shuffle(mlist)
    print("Knowledge of Multiplication level required"
          "" + " " + str(i) + ":")
    #print('\n')
    dlist = [k for k in range(1,13)]
    shuffle(dlist)
    count=0
    ans = []
    for j in mlist:
        for k in dlist:
            if j/k==i or k==i:
                ans.append((j,k))
    #print(ans)
    shuffle(ans)
    for i in range(15):
        print1(ans[i][0],ans[i][1])

    print('\n')


repeats = int(input())
for j in range(repeats):
    for i in range(2,13):
        mult_fn(i)
