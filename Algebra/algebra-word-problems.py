import random


Dict_trader = ['A Trader', 'A man', 'A businessman', 'George', 'Ram', 'Sheela', 'Jim', 'Kelly', 'Krishna', 'Zoya']
Dict_objects = ['Apples', 'Chocolates', 'Cakes', 'box of pears', 'books', 'box of cookies', 'box of blueberries', 'boxes of ice cream', 'pizzas', 'box of beads', 'oranges', 'school bags', 'pencil boxes', 'boxes of carrots']
Dict_change = ['increase','decrease']
n = input("Enter the number of questions you want to generate : ")
try:
    for i in range(int(n)):
        percentage = random.choice([i for i in range(1,99)])
        number = random.choice([i for i in range(11,999)])
        number2 = random.choice([i for i in range(11,999)])
        change = random.choice(Dict_change)
        trader = random.choice(Dict_trader)
        objects = random.choice(Dict_objects)
        print(trader + ' got '+ str(number) +' '+ objects + ' for $' + str(number2) + ' each.')
        print('What is the price of total number of '+ objects + '?')
        print('If the price of '+ objects +' '+ change + ' by '+ str(percentage)+ '%, how much profit or loss in $ will he/she make per item and in total?\n\n')
except ValueError:
    print("Please enter an integer value.")
