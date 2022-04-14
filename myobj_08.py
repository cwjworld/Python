# 测试继承的基本使用

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_age(self):
        print("年龄,年龄,我也不知道")


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)    # 必须显式的调用父类初始化方法，不然解释器不会去调用
        self.score = score


# Student-->Person-->object类
print(Student.mro())

s = Student("陈伟杰", 18, 60)
s.say_age()
print(s.name)