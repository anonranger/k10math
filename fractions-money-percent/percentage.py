import random
words = ["book","water bottle","chair","handbag","TV","shirt","pant","skirt","cupcake","cake"]

perc = ["10", "20", "quarter price 25", "30", "40", "half price 50", "60", "70", "80", "90", "full price 100", "double price 200"]

def print_line(r1,r2,w,v):
    print("If {0}% price of {1} is ${2}".format(r1,w,v))
    print("what is the price of that {0} at {1}%?".format(w,r2))
    print("What is the full price of the",format(w))
    print("Is the {0} selling at a discount or premium?".format(w))
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
i=0
while i<count:
    r1 = random.choice(perc)
    r2 = random.choice(perc)
    if r1==r2:
        continue
    w = random.choice(words)
    v = random.randint(1,10) * random.randint(2,10)
    print_line(r1,r2,w,v)
    i+=1