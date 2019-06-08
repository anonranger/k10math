import random
list1 = ['+','-']
txt = input("Enter the number of questions you want to generate : ")
try:
 val = int(txt)
 C = 'X = '+'Y'+random.choice(list1)+str(random.choice([i for i in range(1,11)]))
 class C():
  def __str__(self):
   return 'X = '+'Y'+random.choice(list1)+str(random.choice([i for i in range(1,11)]))
 for i in range(int(txt)):
  cc= C()
  print(cc)
  st = 'X = '+ str(random.choice([i for i in range(1,11)]))+'Y'
  print(st)
  print("Find X\n\n")
except ValueError:
 print("You have to enter integer value")
