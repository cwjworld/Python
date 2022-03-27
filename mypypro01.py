s = input("请输入一个数字:")

if int(s) < 10:
    print("s是小于10的数字")
else:
    print("s是大于等于10的数字")

#测试三元条件运算符
print("s是小于10的数字" if int(s) < 10 else "s是大于等于10的数字")

