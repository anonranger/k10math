import random
list1 = ['+','-']
txt = input("Enter a the number of questions you want to generate : ")
CC = str(random.choice(['' if i==1 else i for i in range(1,11)]))+'X'+random.choice(list1)+str(random.choice([''if i==1 else i for i in range(1,11)]))+'Y'+' = '+str(random.choice([i for i in range(99,1001)])) 
class CC():
    def __str__(self):
        return str(random.choice(['' if i==1 else i for i in range(1,11)]))+'X'+random.choice(list1)+str(random.choice([''if i==1 else i for i in range(1,11)]))+'Y'+' = '+str(random.choice([i for i in range(99,1001)])) 



A = 'X = '+str(random.choice(['' if i==1 else i for i in range(1,11)]))+'Y'+random.choice(list1)+str(random.choice([i for i in range(1,11)]))
B = 'Y = '+ str(random.choice(['' if i==1 else i for i in range(1,11)]))+'X'+random.choice(list1)+str(random.choice([i for i in range(1,11)]))
C = 'X = '+ str(random.choice([i for i in range(1,11)]))
D = 'Y =' + str(random.choice([i for i in range(1,11)]))
listchoice = [A,B,C,D]

for i in range(int(txt)+1):
    cc= CC()
    print(cc)
    print(random.choice(listchoice) + "\n" + "Find X\nFind Y\n\n\n")

