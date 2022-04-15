# 测试多态

class Man:
    def eat(self):
        print("饿了，吃饭啦！")


class Chinese(Man):
    def eat(self):
        print("中国人用筷子吃饭")


class English(Man):
    def eat(self):
        print("英国人用叉子吃饭")


class India(Man):
    def eat(self):
        print("印度人用右手吃饭")


def manEat(m):
    if isinstance(m, Man):      # isinstance是一个有判断功能的内置函数
        m.eat()         # 多态:一个方法调用，根据对象的不同调用不同的方法！
    else:
        print("不吃饭")

manEat(Chinese())
manEat(English())