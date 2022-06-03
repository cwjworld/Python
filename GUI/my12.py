# pack布局用法

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("700x200")

# Frame是一个矩形区域，用来放置其他子组件
f1 = Frame(root)
f1.pack()
f2 = Frame(root)
f2.pack()

btnText = ("流行乐", "中国风", "日本风", "重金属", "轻音乐")

for txt in btnText:
    Button(f1, text=txt).pack(side="left", padx="10")

for i in range(1, 20):
    Label(f2, width=5, height=10, borderwidth=1, relief="solid",
          bg="black" if i % 2 == 0 else "white").pack(side="left", padx=2)

root.mainloop()