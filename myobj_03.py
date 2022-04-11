# 测试类方法

class Student:
    company = "Bite"  # 类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def printCompany(cls):
        print(cls.company)
    # print(self.name)   #类方法和静态方法中，不能调用实例变量、实例方法


Student.printCompany()

# 测试静态方法


class Student2:
    company = "Bite"  # 类属性

    @staticmethod
    def add(a, b):  # 静态方法
        print("{0}+{1}={2}".format(a, b, (a + b)))
        return a + b


Student2.add(20, 30)