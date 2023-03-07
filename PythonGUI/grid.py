from tkinter import *

root = Tk()

myLabelOne = Label(root, text="Hello World!")
myLabelTwo = Label(root, text="My name is Josip Harci")
myLabelThree = Label(root, text="                         ")

myLabelOne.grid(row=0, column=0)
myLabelTwo.grid(row=1, column=5)
myLabelThree.grid(row=1, column=1)


root.mainloop()

