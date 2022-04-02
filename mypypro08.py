#测试并行迭代

for i in [1,2,3]:
    print(i)

names = ("老大","老二","老三","老四")
ages = (24,20,16,14)
jobs = ("老师","公务员","程序员")

for name,age,job in zip(names,ages,jobs):
    print("{0}--{1}--{2}".format(name,age,job))

for i in range(3):
    print("{0}--{1}--{2}".format(names[i],ages[i],jobs[i]))