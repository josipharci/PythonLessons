from tkinter import *
from tkinter.ttk import *

win = Tk()  
win.title("APP")  
win.geometry("260x150")
win.iconbitmap(r"C:\Users\JosipH\Downloads\favicon.ico")
win.configure(bg='#a0a1ad')

labelname = Label(win , text="Username")
labelname.grid(row = 0, column = 0)


labelpass = Label( win, text="Password")
labelpass.grid(row = 1, column = 0)




win.mainloop()  


