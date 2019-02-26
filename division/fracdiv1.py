import random


def print_line(x,y):
    print("{0}/{1} = ".format(x,y))

def get_count():
    print("Number of questions to generate :")
    try:
        count = int(input())
    except Exception as e:
        print("Incorrect input. Please enter an integer:")
        count = get_count()
    return count


count = get_count()

for i in range(count):
    x1 = random.randint(1,10)
    x2 = random.randint(10,100)
    x3 = random.randint(100,1000)
    x = random.sample([x1,x2,x3],1)
    y = random.randint(2,10)
    if x[0]%y==0:
        y = (y+1)
        if y==10:
            y=2
    print_line(x[0],y)