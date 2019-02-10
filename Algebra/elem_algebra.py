import random


def print_line(c,r1,r2,r3,sign):
    if c==1:
        print("X {0} {1} = {2} , X = ?".format(sign,r1,r3))
        print()
    elif c==2:
        print("{0} = X {1} {2} , X = ?".format(r3,sign ,r1))
        print()
    elif c==3:
        print("{0} {1} X = {2} , X = ?".format(r1, sign, r3))
        print()
    elif c==4:
        print("{0} = {1} {2} X , X = ?".format(r3, r1,sign))
        print()
    elif c==5:
        print("{0}X {1} {2} = {3} , X = ?".format(r1, sign, r2, r3))
        print()
    else:
        print("{0} = {1}X {2} {3} , X = ?".format(r3,r1, sign, r2))
        print()

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
    c = random.randint(1,6)
    r1 = random.randint(1,11)
    r2 = random.randint(1,11)
    r3 = random.randint(1,100)
    s = ['+','-']
    sign = random.choice(s)
    print_line(c,r1,r2,r3,sign)