

def mult_fn(i):
    j = 12
    mr = 1
    while j >= 1:
        mr = i * j
        #print(i)
        #print(j)
        #print(mr)
        print(str(i)+" "+"*"+" "+str(j)+" "+"="+" "+str(mr))
        j = j - 1
        print("\n")
        

input = input('Enter Multiplication table to generate:')
i = int(input)
mult_fn(i)







