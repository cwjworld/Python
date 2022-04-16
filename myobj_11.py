# 对象的浅拷贝和深拷贝
import copy

class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen

class CPU:
    def calculate(self):
        print("啥也不是")
        print("cpu对象: ", self)

class Screen:
    def show10(self):
        print("显示一个好看的画面")
        print("screen对象: ", self)


# 测试变量赋值
c1 = CPU()
c2 = c1
print(c1)
print(c2)

# 测试浅拷贝
s1 = Screen()
m1 = MobilePhone(c1, s1)
m2 = copy.copy(m1)

print(m1, m1.cpu, m1.screen)
print(m2, m2.cpu, m2.screen)

# 测试深拷贝
m3 = copy.deepcopy(m1)
print(m1, m1.cpu, m1.screen)
print(m3, m3.cpu, m3.screen)