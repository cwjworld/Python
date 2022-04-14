# 测试@property装饰器

class Employee:

    @property
    def salary(self):
        print("salary run...")
        return 10000


emp1 = Employee()
# emp1.salary()  传统方法
print(emp1.salary)

print("*********************************")

# 简单使用@property装饰器


class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_salary(self):       # 普通方法
        return self.__salary

    def set_salary(self, salary):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print("录入错误!薪水在1000到50000这个范围")


emp1 = Employee("陈伟杰", 50000)
print(emp1.get_salary())
emp1.set_salary(20000)
print(emp1.get_salary())

print("*********************************")


class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):       # 使用@property装饰器
        return self.__salary

    @salary.setter
    def salary(self,salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("录入错误!薪水在1000到50000这个范围")


emp1 = Employee("陈伟杰", 50000)
print(emp1.salary)
emp1.salary = 2000
print(emp1.salary)