# 测试Label组件的基本用法，使用面向对象的方式

from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)        # super()代表的是父类的定义，而不是父类的对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建新的组件"""
        self.label01 = Label(self, text="比特", width=10, height=2,
                             bg="black", fg="white")
        self.label01.pack()

        self.label02 = Label(self, text="比特", width=10, height=2,
                             bg="blue", fg="white", font=("黑体", 30))
        self.label02.pack()

        # 显示图像 #
        # global = photo        # 把photo声明为全局变量，如果为局部变量，那么本方法执行完后图像对象会销毁，窗口显示不出图像
        # photo = PhotoImage(file="目录/图片文件")
        # self.label03 = Label(self, image=photo)
        # self.label03.pack()

        # 显示多行文本
        self.label04 = Label(self, text="比特\n程序员\n芜湖",
                             borderwidth=1, relief="solid", justify="right")
        self.label04.pack()


if __name__ == "__main__":

    root = Tk()
    root.geometry("400x240+200+300")
    root.title("测试label组件")
    app = Application(master=root)
    root.mainloop()