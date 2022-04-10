class Student:      #类名一般首字母大写，采用驼峰原则

    def __init__(self,name,score):  #self必须位于第一个参数
        self.name = name
        self.score = score

    def say_score(self):
        print("{0}的分数是:{1}".format(self.name,self.score))


s1 = Student("cwj",80)
s1.say_score()

Student.say_score(s1)

print(dir(s1))      #获得所有属性

print(s1.__dict__)      #获得直观上的属性

print(isinstance(s1,Student))