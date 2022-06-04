# coding=utf-8
from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("布局管理place")
root["bg"] = "white"

f1 = Frame(root, width=200, height=200, bg="green")
f1.place(x=30, y=30)

Button(root, text="比特").place(relx=0.2, x=100, y=20, relwidth=0.2, relheight=0.5)
Button(f1, text="程序员").place(relx=0.6, rely=0.7)
Button(f1, text="码农").place(relx=0.5, rely=0.2)
root.mainloop()