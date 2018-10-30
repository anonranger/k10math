from tkinter import *
from tkinter import messagebox
from random import randint
import random
import operator
import sys
import json
import pdfkit
from fpdf import FPDF

top = Tk()
top.title('Project for Arithmetic Study')
w_width = 1200
w_height = 700
top.geometry("1200x700")

class Store:
	def __init__(self, temp):
		self.temp = 0

	def myfunc(self,a):
		self.temp = a

	def myprint(self):
		return self.temp


class Pdf:
	def __init__(self, temp):
		self.temp = ' '
	def myfunc(self,a):
		self.temp = self.temp+" "+a
	def myprint(self):
		return self.temp


class NStore:
	def __init__(self, temp):
		self.temp = 0

	def myfunc(self,a):
		self.temp = a

	def myprint(self):
		return self.temp						

var = Store("0")
pdf = Pdf(' ')
num = NStore("0")

def start():

	lStart = Label(top, text="                 ", bg="#99ffe6")
	lStart.place( x = 130, y = 350)	
	lStart.config(font=("Courier", 24))		

	lcorrectjob = Label(top, text="                      ")
	lcorrectjob.place( x = 400, y = 425)
	lcorrectjob.config(font=("Courier", 24))

	solution_Edit.delete(0, END)

	operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('÷', operator.truediv)]
	op, fn = random.choice(operators)
	op1, fn1 = random.choice(operators)
	x = randint(1, 100) 
	y = randint(1, 100)
	z = randint(1, 10)

	k = randint(1, 2)
	# k = 1
	if k == 1:

		if op == '÷':
			if x > y:
				if x % y == 0:
					ltemplate = str(x) + " ÷ " + str(y) + " ="
					lStart = Label(top, text = ltemplate, bg = "#99ffe6")
					pdf.myfunc(ltemplate)
					lStart.place(x = 130, y = 350)
					lStart.config(font = ("Courier", 24))
					temp = x // y
					pdf.myfunc( ",")
					var.myfunc(temp)
				else:
					x = x * y
					ltemplate = str(x) + " ÷ " + str(y) + " ="
					lStart = Label(top, text = ltemplate, bg = "#99ffe6")
					pdf.myfunc(ltemplate)
					lStart.place(x = 130, y = 350)
					lStart.config(font = ("Courier", 24))
					temp = x // y
					pdf.myfunc( ",")
					var.myfunc(temp)
			elif x < y:
				x = x * y			
				lStart = Label(top, text="{} {} {} = ".format(x, op, y), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))		
				temp = x // y
				pdf.myfunc(",")
				var.myfunc(temp)
		elif op == '-':
			if x > y:
				lStart = Label(top, text = "{} {} {} = ".format(x, op, y), bg = "#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))		
				temp = fn(x, y)
				pdf.myfunc(",")
				var.myfunc(temp)
			else:
				t = x
				x = y
				y = t
				lStart = Label(top, text = "{} {} {} = ".format(x, op, y), bg = "#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))		
				temp = fn(x, y)
				pdf.myfunc(",")
				var.myfunc(temp)			
		else:
			
			lStart = Label(top, text="{} {} {} = ".format(x, op, y), bg="#99ffe6")
			pdf.myfunc(str(x)+op+str(y)+"=")
			lStart.place( x = 130, y = 350)
			lStart.config(font=("Courier", 24))
			temp = fn(x, y)	
			pdf.myfunc(",")				
			var.myfunc(temp)			
						
	else:
		
		if op == '+' and op1 == '÷':
			if y > z:
				if y % z == 0:
					ltemplate = str(x) + " + " + "("+ str(y) + " ÷ " + str(z)+")" + " = "
					lStart = Label(top, text = ltemplate, bg = "#99ffe6")
					pdf.myfunc(ltemplate)
					lStart.place(x = 130, y = 350)
					lStart.config(font = ("Courier", 24))
					t = y // z
					temp = x + t
					pdf.myfunc( ",")
					var.myfunc(temp)
				else:
					y = y * z
					ltemplate = str(x) + " + " +"("+ str(y) + " ÷ " + str(z)+")" + " = "
					lStart = Label(top, text = ltemplate, bg = "#99ffe6")
					pdf.myfunc(ltemplate)
					lStart.place(x = 130, y = 350)
					lStart.config(font = ("Courier", 24))
					t = y // z
					temp = x + t
					pdf.myfunc(",")
					var.myfunc(temp)
			
		elif op == '+' and op1 == '-':
			if (x + y) > z:
				
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = fn1(fn(x, y), z)
				pdf.myfunc(",")
				var.myfunc(temp)
			elif (x + Y) < z:
				t = x
				x = z
				z = t
				
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = fn1(fn(x, y), z)
				pdf.myfunc(",")	
				var.myfunc(temp)
		elif op == '+' and op1 == '*':
			ltemplate = str(x) +" + "+ "(" +str(y)+" * " + str(z) + ")"+ " = "
			lStart = Label(top, text=ltemplate, bg="#99ffe6")
			pdf.myfunc(ltemplate)
			lStart.place( x = 130, y = 350)
			lStart.config(font=("Courier", 24))
			temp = fn(x, fn1(y,z))
			pdf.myfunc(",")
			var.myfunc(temp)	
		elif op =='-' and op1 == '+':
			if (x + z) < y:
				t = y
				y = x
				x = t
				
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op1, y, op, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = fn1(fn(x, y), z)
				pdf.myfunc(",")
				var.myfunc(temp)
			else:
				
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)	
				lStart.config(font=("Courier", 24))
				temp = fn1(fn(x, y), z)
				pdf.myfunc(",")
				var.myfunc(temp)
		elif op == '-' and op1 == '-':
			if x < (y + z):
				x = y + z + 2
				
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = fn1(fn(x, y), z)
				pdf.myfunc(",")
				var.myfunc(temp)
			else:			
					
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = fn1(fn(x, y), z)
				pdf.myfunc(",")
				var.myfunc(temp)
		elif op == '-' and op1 == '÷':
			if y % z == 0:
				if x > y//z:
					ltemplate = str(x) +" - "+ "(" +str(y)+" ÷ " + str(z) + ")"+ " = "
					lStart = Label(top, text=ltemplate, bg="#99ffe6")
					pdf.myfunc(ltemplate)
					lStart.place( x = 130, y = 350)
					lStart.config(font=("Courier", 24))
					temp = fn(x, y//z)
					pdf.myfunc(",")
					var.myfunc(temp)
				else:
					x = x + y//z
					ltemplate = str(x) +" - "+ "(" +str(y)+" ÷ " + str(z) + ")"+ " = "
					lStart = Label(top, text=ltemplate, bg="#99ffe6")
					pdf.myfunc(ltemplate)
					lStart.place( x = 130, y = 350)
					lStart.config(font=("Courier", 24))
					temp = fn(x, y//z)
					pdf.myfunc(",")
					var.myfunc(temp)				
			else:
				y = y * z
				ltemplate = str(x) +" - "+ "(" +str(y)+" ÷ " + str(z) + ")"+ " = "
				lStart = Label(top, text=ltemplate, bg="#99ffe6")
				pdf.myfunc(ltemplate)
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = fn(x, y//z)
				pdf.myfunc(",")
				var.myfunc(temp)
		elif op == '-' and op1 == '*':
			if x > y*z:
				ltemplate = str(x) + " - " +"(" + str(y) + " * " + str(z) +")" + "="
				lStart = Label(top, text=ltemplate, bg="#99ffe6")
				pdf.myfunc(ltemplate)
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = fn(x,fn1(y, z))	
				pdf.myfunc(",")						
				var.myfunc(temp)
			elif x < y*z:
				x = y*z + x
				ltemplate = str(x) + " - " +"(" + str(y) + " * " + str(z) +")" + "="
				lStart = Label(top, text=ltemplate, bg="#99ffe6")
				pdf.myfunc(ltemplate)
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = fn(x,fn1(y, z))	
				pdf.myfunc(",")						
				var.myfunc(temp)
		elif op == '*' and op1 == '+':
			lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
			pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
			lStart.place( x = 130, y = 350)
			lStart.config(font=("Courier", 24))
			temp = fn1(fn(x, y), z)	
			pdf.myfunc(",")
			var.myfunc(temp)
		elif op == '*' and op1 == '-':
			lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
			pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
			lStart.place( x = 130, y = 350)
			lStart.config(font=("Courier", 24))
			temp = fn1(fn(x, y), z)	
			pdf.myfunc(",")
			var.myfunc(temp)
		elif op == '*' and op1 == '÷':
			if y % z == 0:
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = fn(x, y)//z
				pdf.myfunc(",")
				var.myfunc(temp)
			else:
				y = y*z					
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = fn(x, y)//z	
				pdf.myfunc(",")
				var.myfunc(temp)
		elif op == '÷' and op1 == '+':
			if x % y == 0:
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = x//y + z	
				pdf.myfunc(",")
				var.myfunc(temp)
			else:
				x = x * y
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = x//y + z		
				pdf.myfunc(",")
				var.myfunc(temp)
		elif op == '÷' and op1 == '-':
			if x % y == 0:
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = x//y - z		
				pdf.myfunc(",")
				var.myfunc(temp)
			else:
				x = x * y
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = x//y - z	
				pdf.myfunc(",")
				var.myfunc(temp)
		elif op == '÷' and op1 == '*':
			if x % y == 0:
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = fn1(x//y, z)	
				pdf.myfunc(",")
				var.myfunc(temp)
			else:
				x = x * y
				lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				lStart.place( x = 130, y = 350)
				lStart.config(font=("Courier", 24))
				temp = fn1(x//y, z)	
				pdf.myfunc(",")
				var.myfunc(temp)
		elif op == '÷' and op1 == '÷':	
			if x % y == 0:
				t = x//y
				if t%z == 0:
					lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
					pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
					lStart.place( x = 130, y = 350)
					lStart.config(font=("Courier", 24))
					temp = t//z	
					pdf.myfunc(",")
					var.myfunc(temp)
				else:
					x = x*z
					t = x//y
					lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
					pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
					lStart.place( x = 130, y = 350)
					lStart.config(font=("Courier", 24))
					temp = t//z
					pdf.myfunc(",")
					var.myfunc(temp)	
			else:				
				x = x * y
				t = x//y
				if t%z == 0:
					lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
					pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
					lStart.place( x = 130, y = 350)
					lStart.config(font=("Courier", 24))
					temp = t//z	
					pdf.myfunc(",")
					var.myfunc(temp)
				else:
					x = x*z
					tt = x//y

					lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
					pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
					lStart.place( x = 130, y = 350)
					lStart.config(font=("Courier", 24))
					temp = tt//z	
					pdf.myfunc(",")
					var.myfunc(temp)	
												
		else:

			lStart = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
			pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
			lStart.place( x = 130, y = 350)
			lStart.config(font=("Courier", 24))
			temp = fn1(fn(x, y), z)	
			pdf.myfunc(",")
			var.myfunc(temp)		

def JSONtoPDF(json_data):
    
	data = json_data.split(",")
	print_number = printNumber_Edit.get()
	p_number = int(print_number)

	pdf = FPDF()
	pdf.set_font('arial', 'B', 30.0)
	pdf.add_page()
	pdf.set_xy(7, 20)
	for index in range(len(data)):
		if index > p_number:
			break
		if index < p_number:
			pdf.cell(ln=1, h=20.0, align='L', w=0, txt=data[index], border=0)
	# for x in json_data.split(","):	
	# 	pdf.cell(ln=1, h=20.0, align='L', w=0, txt=x, border=0)
						
	pdf.output('test.pdf', 'F')
    
def prints():
	rprint_number = printNumber_Edit.get()
	rp_number = int(rprint_number)

	for x in range(rp_number):
		start()
		x = pdf.myprint()
		print(x)

	json_data = pdf.myprint()
	JSONtoPDF(json_data)

def check():

	edit_number = solution_Edit.get()
	var_real = str(var.myprint())

	if var_real == edit_number:
		lcorrectjob = Label(top, text="Correct - Good Job")
		lcorrectjob.place( x = 400, y = 425)
		lcorrectjob.config(font=("Courier", 24))
		
	elif var_real != edit_number:
		lwrongAgain = Label(top, text="Wrong -  Try Again")
		lwrongAgain.place( x = 400, y = 425)
		lwrongAgain.config(font=("Courier", 24))	
		
bnewNumber = Button(top, text = "New Number", command = start, font=("Courier", 18), bg = "#ccfff2")
bnewNumber.place(x = 850 ,y = 350)
bnewNumber.config(width = 13, height = 1)

bCheck = Button(top, text = "Check", command = check, font=("Courier", 18), bg = "#ccfff2")
bCheck.place(x = 630,y = 350)
bCheck.config(width = 13, height = 1)

bPrint = Button(top, text = "Print", command = prints, font=("Courier", 18), bg = "#ccfff2")
bPrint.place(x = 780,y = 500)
bPrint.config(width = 8, height = 1)

lmathNinja = Label(top, text = "Math Ninja", font=("Courier", 24), bg = "#80d4ff")
lmathNinja.place(x = 450,y = 120)
lmathNinja.config(width = 15, height = 2)

lmathOperation = Label(top, text = "Basic Math Operations", font=("Courier", 14))
lmathOperation.place(x = 475, y = 200)
lmathOperation.config(width = 22, height = 2)

x = 34 
y = 17
l = str(x) + "  +  " + str(y) + "  ="
lStart = Label(top, text=l, bg = "#99ffe6")
temp = x + y
var.myfunc(temp)
pdf.myfunc(l+",")
lStart.place( x = 130, y = 350)
lStart.config(font=("Courier", 24), height = 1, width = 17)

solution_Edit = Entry(top, bd =2, width = 6, bg = "#99ffe6")
solution_Edit.place( x = 480, y = 350)
solution_Edit.config(font=("Courier", 24))

printNumber_Edit = Entry(top, bd =2, width = 3, bg = "#99ffe6")
printNumber_Edit.place( x = 680, y = 500)
printNumber_Edit.config(font=("Courier", 24))

top.mainloop()

