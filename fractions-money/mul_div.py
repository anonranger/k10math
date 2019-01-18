from random import randint
from random import shuffle

l = [10,100,1000,10000]

ans = []

for i in range(10):
    shuffle(l)
    ans.append(str(randint(0,1000)) + '/' + str(l[0]) + " =")

for i in range(10):
    shuffle(l)
    ans.append(str(randint(0,1000)/l[1]) + '*' + str(l[0]) + " =")

shuffle(ans)
for i in ans:
    print(i)