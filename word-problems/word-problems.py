import random
words = ["books","water bottles","chairs","handbags","TVs","shirts","pants","skirts","cupcakes","cakes"]

def print_line(c,r1,r2,w,v):
    if c==1:
        print("If {0} {1} cost ${2}".format(r1,w,v))
        print("How much does {0} {1} cost?".format(r2,w))
        print()
    else:
        print("If it costs ${0} for {1} {2}".format(v, r1,w, v))
        print("How much does {0} {1} cost?".format(r2, w))
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
    r1 = random.randint(1,10)
    r2 = random.randint(1,10)
    c = random.randint(1,3)
    if r1==r2:
        if r1==10:
            r1 = 2
        else:
            r2 = (r2+1)
    w = random.choice(words)
    v = r1 * random.randint(2,10)
    print_line(c,r1,r2,w,v)