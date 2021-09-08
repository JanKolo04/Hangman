from tkinter import *
from tkmacosx import *
import os
import random

root = Tk()
root.title('Hangman Game')
root.geometry('440x400')
root.resizable(0,0)


with open('passwords.txt') as f:
	lines = f.readlines()

randomowe = ''.join(random.choice(lines))

litery = []



while True:
	for i in randomowe:
		if i.lower() in litery:
			char = Text(root)
			char.pack()
		else:
			underlines = Text(root)
			underlines.pack()


root.mainloop()