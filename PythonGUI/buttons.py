from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

myButton = Button(root,text="Click Me!",padx=20,pady=10, command=myClick ,fg="blue" , bg="red")
myButton.pack()


root.mainloop()



