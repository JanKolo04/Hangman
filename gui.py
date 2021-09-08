from tkinter import *
from tkmacosx import *
import os
import random

root = Tk()
root.title('Hangman Game')
root.geometry('440x400')
root.resizable(0,0)


#exit button
Exit = Button(root, text='Exit', bg="red", fg="black", command=root.destroy)
Exit.pack()
Exit.place(x=5, y=5, height=30, width=50)



with open('passwords.txt') as f:
	lines = f.readlines()

randomowe = ''.join(random.choice(lines))

chances = 5
litery = []

done = False
while not done:
	for i in randomowe:
		if i.lower() in litery:
			print(i, end=' ')
		else:
			print('_', end=' ')

	litera = input(f'\nLeft {chances} chances, Guess char: ')
	print('')
	litery.append(litera.lower())

	if litera.lower() not in randomowe.lower():
		chances -= 1
		if chances == 0:
			break


	done = True
	for i in randomowe:
		if i.lower() not in litery:
			done = False

if done:
	print('You win')
else:
	print('You lose')

root.mainloop()