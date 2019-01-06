import random

a = ['0','00','000']
def get_rand(a,b):
    return str(random.randint(a,b))

for j in range(int(input())):
    print("Sub-zero")
    print()
    for i in range(20):
        random.shuffle(a)
        A = get_rand(1,9) + a[0]
        if int(get_rand(0,1)):
            A += get_rand(1,9)
        B = get_rand(1, int(A))
        print(A + " - " + B + " = ")
    print()


