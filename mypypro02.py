#测试多分支选择结构
score = int(input("请输入分数: "))
grade = ""

if score < 60:
    grade = "不及格"
elif score < 80:  #60-80之间
    grade = "及格"
elif score < 90:
    grade = "良好"
else:
    grade = "优秀"

print("分数是{0}, 等级是{1}".format(score, grade))

print("*******************************************************")

#测试选择结构的嵌套
score = int(input("请输入一个0-100之间的分数: "))
if score > 100 or score < 0:
    score = int(input("输入错误!请重新输入一个0-100之间的数字: "))
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "E"
    print("分数是{0}, 等级是{1}".format(score, grade))

print("*******************************************************")

score = int(input("请输入一个0-100之间的分数: "))
degree = "ABCDE"
if score > 100 or score < 0:
    score = int(input("输入错误!请重新输入一个0-100之间的数字"))
else:
    num = score // 10
    if num < 6:
        num = 5

    print("分数是{0}, 等级是{1}".format(score, degree[9 - num]))