#测试break
while True:
    a = input("请输入一个字符(输入Q或者q的时候退出): ")
    if a == "q" or a == "Q":
        print("循环结束，退出")
        break
    else:
        print(a)

print("****************************************************")

#break和continue小练习
empNum = 0
salarySum = 0
salarys = []
while True:
    s = input("请输入员工的薪资(按q或者Q结束)")

    if s.upper() == 'Q':
        print("录入完毕，退出")
        break
    if float(s) < 0:
        continue
    empNum += 1
    salarys.append(float(s))
    salarySum += float(s)

print("员工数{0}".format(empNum))
print("录入薪资", salarys)
print("平均薪资{0}".format(salarySum/empNum))

