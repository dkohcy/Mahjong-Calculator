from Tkinter import *


class sian:

	def __init__(self, master):


		frame = Frame(master, width = 100, height = 100, bg='red')
		frame.grid(column =3, row = 0)

		scrollbar = Scrollbar(master)
		scrollbar.grid(column = 2, row = 0)

		listbox1 = Listbox(frame,width = 5, height = 20, yscrollcommand = scrollbar.set)
		for i in range(100):
			listbox1.insert(END, str(i))

		listbox1.grid(column = 1, row= 0)

		listbox2 = Listbox(master,width = 10, height = 20, yscrollcommand = scrollbar.set)
		for i in range(100):
			listbox2.insert(END, str(i))



		listbox2.grid(column = 2, row= 0)

		scrollbar.config(command = listbox1.yview)
		scrollbar.config(command = listbox2.yview)











master = Tk()
myGui = sian(master)
master.mainloop()