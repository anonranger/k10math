from tkinter import *
from tkinter import messagebox
from random import randint
import random
import operator
import sys
import json
import pdfkit
from fpdf import FPDF

#from PDFWriter import PDFWriter
# from PyPDF2 import PdfFileReader, PdfFileWriter
# from PyPDF2 import PdfFileReader
# import pyPdf

top = Tk()
top.title('Project for Arithmetic Study')
w_width = 1200
w_height = 700
top.geometry("1200x700")

# fm = Frame(top, width=w_width, height=w_height, bg="#0080ff")
# fm.pack(side=TOP, expand=NO, fill=NONE)

# fm = Frame(top, width=800, height=600, bg="blue")
# fm.pack(side=TOP, expand=NO, fill=NONE)

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

	L1 = Label(top, text="                 ", bg="#99ffe6")
	L1.place( x = 130, y = 350)	
	L1.config(font=("Courier", 24))	

	# i = num.myprint() + 1
	# num.myfunc(i)
	# L2 = Label(top, text = str(num.myprint()), bg="#99ffe6") 
	# L2.place(x = 680, y = 500)
	# L2.config(width = 3)
	# L2.config(font=("Courier", 24), height = 1)	

	L3 = Label(top, text="                      ")
	L3.place( x = 400, y = 425)
	L3.config(font=("Courier", 24))

	E1.delete(0, END)

	operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
	op, fn = random.choice(operators)
	op1, fn1 = random.choice(operators)
	x = randint(1, 100) 
	y = randint(1, 100)
	z = randint(1, 10)

	k = randint(1, 2)
	# k = 1
	if k == 1:

		if op == '-':
			if x > y:
				if x % y == 0:
					l1 = str(x) + " ÷ " + str(y) + " ="
					L1 = Label(top, text = l1, bg = "#99ffe6")
					pdf.myfunc(l1)
					L1.place(x = 130, y = 350)
					L1.config(font = ("Courier", 24))
					temp = x // y
					pdf.myfunc( ",")
					# str(temp) +
					var.myfunc(temp)
				else:
					x = x * y
					l1 = str(x) + " ÷ " + str(y) + " ="
					L1 = Label(top, text = l1, bg = "#99ffe6")
					pdf.myfunc(l1)
					L1.place(x = 130, y = 350)
					L1.config(font = ("Courier", 24))
					temp = x // y
					pdf.myfunc( ",")
					var.myfunc(temp)
			elif x < y:
				t = x 
				x = y
				y = t
				
				L1 = Label(top, text="{} {} {} = ".format(x, op, y), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+"=")
				L1.place( x = 130, y = 350)
				L1.config(font=("Courier", 24))		
				temp = fn(x, y)
				pdf.myfunc(",")
				var.myfunc(temp)
		else:
			
			L1 = Label(top, text="{} {} {} = ".format(x, op, y), bg="#99ffe6")
			pdf.myfunc(str(x)+op+str(y)+"=")
			L1.place( x = 130, y = 350)
			L1.config(font=("Courier", 24))
			temp = fn(x, y)	
			pdf.myfunc(",")				
			var.myfunc(temp)			
						
	else:
		# L1 = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z))
		# L1.place( x = 80, y = 200)
		if op == '+' and op1 == '+':
			if y > z:
				if y % z == 0:
					l1 = str(x) + " + " + "("+ str(y) + " ÷ " + str(z)+")" + " = "
					L1 = Label(top, text = l1, bg = "#99ffe6")
					pdf.myfunc(l1)
					L1.place(x = 130, y = 350)
					L1.config(font = ("Courier", 24))
					t = y // z
					temp = x + t
					pdf.myfunc( ",")
					var.myfunc(temp)
				else:
					y = y * z
					l1 = str(x) + " + " +"("+ str(y) + " ÷ " + str(z)+")" + " = "
					L1 = Label(top, text = l1, bg = "#99ffe6")
					pdf.myfunc(l1)
					L1.place(x = 130, y = 350)
					L1.config(font = ("Courier", 24))
					t = y // z
					temp = x + t
					pdf.myfunc(",")
					var.myfunc(temp)
			
		elif op == '+' and op1 == '-':
			if (x + y) > z:
				
				L1 = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				L1.place( x = 130, y = 350)
				L1.config(font=("Courier", 24))
				temp = fn1(fn(x, y), z)
				pdf.myfunc(",")
				var.myfunc(temp)
			elif (x + Y) < z:
				t = x
				x = z
				z = t
				
				L1 = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				L1.place( x = 130, y = 350)
				L1.config(font=("Courier", 24))
				temp = fn1(fn(x, y), z)
				pdf.myfunc(",")	
				var.myfunc(temp)
		elif op == '+' and op1 == '*':
			l1 = str(x) +" + "+ "(" +str(y)+" * " + str(z) + ")"+ " = "
			L1 = Label(top, text=l1, bg="#99ffe6")
			pdf.myfunc(l1)
			L1.place( x = 130, y = 350)
			L1.config(font=("Courier", 24))
			temp = fn(x, fn1(y,z))
			pdf.myfunc(",")
			var.myfunc(temp)	
		elif op =='-' and op1 == '+':
			if (x + z) < y:
				t = y
				y = x
				x = t
				
				L1 = Label(top, text="{} {} {} {} {} = ".format(x, op1, y, op, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				L1.place( x = 130, y = 350)
				L1.config(font=("Courier", 24))
				temp = fn1(fn(x, y), z)
				pdf.myfunc(",")
				var.myfunc(temp)
			else:
				
				L1 = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				L1.place( x = 130, y = 350)	
				L1.config(font=("Courier", 24))
				temp = fn1(fn(x, y), z)
				pdf.myfunc(",")
				var.myfunc(temp)
		elif op == '-' and op1 == '-':
			if x < (y + z):
				x = y + z + 2
				
				L1 = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				L1.place( x = 130, y = 350)
				L1.config(font=("Courier", 24))
				temp = fn1(fn(x, y), z)
				pdf.myfunc(",")
				var.myfunc(temp)
			else:			
					
				L1 = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
				pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
				L1.place( x = 130, y = 350)
				L1.config(font=("Courier", 24))
				temp = fn1(fn(x, y), z)
				pdf.myfunc(",")
				var.myfunc(temp)
		elif op == '-' and op1 == '*':
			if x < y*z:
				t = x
				x = y
				y = z 
				z = t
				l1 = str(x) + " - " +"(" + str(y) + " * " + str(z) +")" + "="
				L1 = Label(top, text=l1, bg="#99ffe6")
				pdf.myfunc(l1)
				L1.place( x = 130, y = 350)
				L1.config(font=("Courier", 24))
				temp = fn(fn1(x,y), z)	
				pdf.myfunc(",")						
				var.myfunc(temp)
		elif op == '*' and op1 == '+':
			L1 = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
			pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
			L1.place( x = 130, y = 350)
			L1.config(font=("Courier", 24))
			temp = fn1(fn(x, y), z)	
			pdf.myfunc(",")
			var.myfunc(temp)
		else:

			L1 = Label(top, text="{} {} {} {} {} = ".format(x, op, y, op1, z), bg="#99ffe6")
			pdf.myfunc(str(x)+op+str(y)+op1+str(z)+"=")
			L1.place( x = 130, y = 350)
			L1.config(font=("Courier", 24))
			temp = fn1(fn(x, y), z)	
			pdf.myfunc(",")
			var.myfunc(temp)		

def JSONtoPDF(json_data):
    # Get the data values from the JSON string json_data.
	#pdfkit.from_string('MicroPyramid', 'micro.pdf')
	# print(json_data)
	data = json_data.split(",")
	print(data)
	print_number = E2.get()
	p_number = int(print_number)
	
	pdf = FPDF()
	pdf.set_font('arial', 'B', 30.0)
	pdf.add_page()
	pdf.set_xy(7, 20)
	for index in range(len(data)):
		if index > p_number:
			print(index)
			break
		if index < p_number:
			pdf.cell(ln=1, h=20.0, align='L', w=0, txt=data[index], border=0)
	# for x in json_data.split(","):	
	# 	pdf.cell(ln=1, h=20.0, align='L', w=0, txt=x, border=0)
						
	pdf.output('test.pdf', 'F')
    
def prints():
    
    json_data = pdf.myprint()
    
    JSONtoPDF(json_data)

def check():

	edit_number = E1.get()
	var_real = str(var.myprint())

	if var_real == edit_number:
		L1 = Label(top, text="Correct - Good Job")
		L1.place( x = 400, y = 425)
		L1.config(font=("Courier", 24))
		
	elif var_real != edit_number:
		L1 = Label(top, text="Wrong -  Try Again")
		L1.place( x = 400, y = 425)
		L1.config(font=("Courier", 24))	
		
B1 = Button(top, text = "New Number", command = start, font=("Courier", 18), bg = "#ccfff2")
B1.place(x = 850 ,y = 350)
B1.config(width = 13, height = 1)

B2 = Button(top, text = "Check", command = check, font=("Courier", 18), bg = "#ccfff2")
B2.place(x = 630,y = 350)
B2.config(width = 13, height = 1)

B3 = Button(top, text = "Print", command = prints, font=("Courier", 18), bg = "#ccfff2")
B3.place(x = 780,y = 500)
B3.config(width = 8, height = 1)

L3 = Label(top, text = "Math Ninja", font=("Courier", 24), bg = "#80d4ff")
L3.place(x = 450,y = 120)
L3.config(width = 15, height = 2)

L4 = Label(top, text = "Basic Math Operations", font=("Courier", 14))
L4.place(x = 475, y = 200)
L4.config(width = 22, height = 2)

x = 34 
y = 17
l = str(x) + "  +  " + str(y) + "  ="
L1 = Label(top, text=l, bg = "#99ffe6")
temp = x + y
var.myfunc(temp)
pdf.myfunc(l+",")
L1.place( x = 130, y = 350)
L1.config(font=("Courier", 24), height = 1, width = 17)

# L2 = Label(top, text = "  ", bg = "#99ffe6")
# L2.place(x = 680, y = 500)
# L2.config(width = 3)
# L2.config(font=("Courier", 24), height = 1)

E1 = Entry(top, bd =2, width = 6, bg = "#99ffe6")
E1.place( x = 480, y = 350)
E1.config(font=("Courier", 24))

E2 = Entry(top, bd =2, width = 3, bg = "#99ffe6")
E2.place( x = 680, y = 500)
E2.config(font=("Courier", 24))

top.mainloop()

