from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#e.insert(0, "")

def button_click(number):
    current = e.get()
    e.insert(0, str(current) + str(number))
    return

# Define Buttons

buttonOne = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
buttonTwo = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
buttonThree = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
buttonFour = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
buttonFive = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
buttonSix = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
buttonSeven = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
buttonEight = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
buttonNine = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
buttonZero = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_click())
button_equal = Button(root, text="=", padx=91, pady=20, command=lambda: button_click())
button_clear = Button(root, text="Clear", padx=79, pady=20, command=lambda: button_click())




# Put the buttons on the screen

buttonOne.grid(row=3, column=0)
buttonTwo.grid(row=3, column=1)
buttonThree.grid(row=3, column=2)

buttonFour.grid(row=2, column=0)
buttonFive.grid(row=2, column=1)
buttonSix.grid(row=2, column=2)

buttonSeven.grid(row=1, column=0)
buttonEight.grid(row=1, column=1)
buttonNine.grid(row=1, column=2)

buttonZero.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)




root.mainloop()