# coding=utf-8
# 测试自定义异常类

class AgeError(Exception):   #继承Exception
    def __init__(self, errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo
    def __str__(self):
        return str(self.errorInfo)+",年龄错误!"


#################测试代码##################
if __name__ == "__main__":   #如果为True，则模块是作为独立文件运行，可以执行测试代码
    age = int(input("输入一个年龄:"))
    if age<1 or age>150:
        raise AgeError(age)
    else:
        print("正常的年龄：", age)




