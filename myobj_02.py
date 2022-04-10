#测试类属性:内存分析创建类和对象的底层
class Student:

    school = "Bite"   #类属性
    count = 0   #类属性

    def __init__(self,name,score):
        self.name = name        #实例属性
        self.score = score
        Student.count = Student.count+1

    def say_score(self):     #实例方法
        print("我的学校是:", Student.school)
        print(self.name,'的分数是:',self.score)


s1 = Student('张三',80)         #s1是实例对象，自动调用__init__()方法
s1.say_score()

s2 = Student("李四",60)
s3 = Student("王五",100)

print('一共创建{0}个Student对象'.format(Student.count))