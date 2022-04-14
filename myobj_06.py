# 测试私有属性、私有方法

class Employee:

    __company = "程序员"

    def __init__(self, name, age):
        self.name = name
        self.__age = age    # 私有属性

    def __work(self):   # 私有方法
        print("好好学习，天天向上!")
        print("年龄:{0}".format(self.__age))
        print(Employee.__company)


e = Employee("陈伟杰", 20)

print(e.name)
print(e._Employee__age)
print(dir(e))
e._Employee__work()
print(Employee._Employee__company)
