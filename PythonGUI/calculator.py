from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#e.insert(0, "")

def button_add():
    return

buttonOne = Button(root, text="1", padx=40, pady=20, command=button_add)
buttonTwo = Button(root, text="2", padx=40, pady=20, command=button_add)
buttonThree = Button(root, text="3", padx=40, pady=20, command=button_add)
buttonFour = Button(root, text="4", padx=40, pady=20, command=button_add)
buttonFive = Button(root, text="5", padx=40, pady=20, command=button_add)
buttonSix = Button(root, text="6", padx=40, pady=20, command=button_add)
buttonSeven = Button(root, text="7", padx=40, pady=20, command=button_add)
buttonEight = Button(root, text="8", padx=40, pady=20, command=button_add)
buttonNine = Button(root, text="9", padx=40, pady=20, command=button_add)
buttonZero = Button(root, text="0", padx=40, pady=20, command=button_add)

myButton = Button(root,  text="Enter Your Stock Quote",  command=myClick)


root.mainloop()