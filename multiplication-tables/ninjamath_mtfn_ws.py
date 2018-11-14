

def mult_fn(i):
    j = 12
    mr = 1
    while j >= 1:
        mr = i * j
        #print(i)
        #print(j)
        #print(mr)
        #Worksheet hide result
        print(str(i)+" "+"*"+" "+str(j)+" "+"="+" ")
        j = j - 1
        print("\n")
        

input = input('Enter Multiplication table to generate:')
i = int(input)
mult_fn(i)







