import random
k = 1
print("ADD AND SUBTRACT TWO DIGIT NUMBERS:")
print("/n")
while (k <= 2000):
    i = random.randint(10,99)
    j = random.randint(1,99)
    operator = ['+', '-']
    co=random.choice(operator)
    print(str(i)+" "+str(co)+" "+str(j)+" "+"=")
    print("/n")
    k = k + 1

    








