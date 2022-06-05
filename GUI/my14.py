# 扑克牌游戏界面的设计

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 通过place布局管理器哦实现扑克牌位置的控制
        # self.photo = PhotoImage(file="photo/puke/puke01.jpg")
        # self.puke01 = Label(self.master, image=self.photo)
        # self.puke01.place(x=10, y=50)

        self.photos = [PhotoImage(file="photo/puke/puke"+str(i+1)+".jpg") for i in range(8)]
        self.pukes = [Label(self.master, image=self.photos[i]) for i in range(8)]

        for i in range(8):
            self.pukes[i].place(x=10+i*40, y=50)

        # 为所有的Label增加事件处理
        self.pukes[0].bind_class("Label", "<Button-1>", self.chupai)

    def chupai(self, event):
        print(event.widget.winfo_geometry())
        print(event.widget.winfo_y())

        if event.widget.winfo_y() == 50:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)


if __name__ == '__main__':
    root = Tk()
    root.geometry("600x270+200+300")
    app = Application(master=root)
    root.mainloop()
