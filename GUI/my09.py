# 测试Canvas组件的基本用法，使用面向对象的方式

import random
from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.canvas =Canvas(self, width=300, height=200, bg="green")
        self.canvas.pack()
        # 画一条直线
        line = self.canvas.create_line(10, 10, 20, 20, 30, 30)
        # 画一个矩形
        rect = self.canvas.create_rectangle(50, 50, 100, 100)
        # 画一个圆，坐标为两双。为椭圆的边界矩形左上角和底部右下角
        oval =self.canvas.create_oval(50, 50, 100, 100)

        Button(self, text="画十个矩形", command=self.draw50Recg).pack(side="left")

    def draw50Recg(self):
        for i in range(0, 1000):
            x1 = random.randrange(int(self.canvas["width"])/2)
            y1 = random.randrange(int(self.canvas["width"])/2)
            x2 = x1 + random.randrange(int(self.canvas["width"])/2)
            y2 = y1 + random.randrange(int(self.canvas["width"])/2)
            self.canvas.create_rectangle(x1, y1, x2, y2)


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300+200+300")
    app = Application(master=root)
    root.mainloop()
