from tkinter import *

class Buttons:
	
	def __init__ (self, master): 
		
		frame = Frame(master)
		frame.pack()
		
		self.v = IntVar()
		self.e = Entry(master)
		self.e.pack()
		self.but = Button(master, text="Enter", width = 10, command=self.printmessage)
		self.but.pack()	
		for num in range (0,10):
			self.e2 = Entry(master)
			self.e2.pack()
			self.e2.focus_set()
			self.but2 = Button(root, text="Enter 2", width = 10, command=self.printmessage2)
			self.but2.pack()
		
		self.budgetButton = Button(frame, text="Set Up Budget")
		self.budgetButton.pack()
		
		self.viewButton = Button(frame, text="View Budget")
		self.viewButton.pack()
		
		self.exit = Button(frame, text="Exit", command=frame.quit)
		self.exit.pack()
	def entercats (self):
		
	def printmessage (self):
		print (self.e.get())
	def printmessage2 (self):
		print (self.e2.get())
		
root = Tk()
main = Buttons(root)
root.mainloop()