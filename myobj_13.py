# 设计模式 —— 单例模式的实现

class MySingleton:

    __obj = None  # 类属性
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, name):
        if MySingleton.__init_flag:
            print("init....")
            self.name = name
            MySingleton.__init_flag = False


a = MySingleton("a")
b = MySingleton("b")
c = MySingleton("c")
print(a)
print(b)
print(c)
