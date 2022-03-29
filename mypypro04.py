#测试for循环
for x in (10,20,30):
    print(x * 30)

print("****************************************************")

#遍历字符串
for y in "abcdefg":
    print(y)

print("****************************************************")

#遍历字典
d = {"name":"陈伟杰", "age":19, "job":"程序员"}
for x in d:
    print(x)
for x in d.keys():
    print(x)
for x in d.values():
    print(x)
for x in d.items():
    print(x)

print("****************************************************")

#range对象
for x in range(5):
    print(x)

print("****************************************************")

#利用for循环计算1-100之间数字的累加和，1-100之间奇偶数分别的累加和
sum_all = 0
sum_odd = 0
sum_even = 0
for x in range(101):
    sum_all += x
    if x % 2 == 1:
        sum_odd += x
    else:
       sum_even += x
print("1-100累加总和是{0}，奇数和是{1},偶数和是{2}".format(sum_all, sum_odd, sum_even))


