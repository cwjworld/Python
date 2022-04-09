#测试递归函数基本原理
#如果无限制调用自己会产生循环最后超出栈空间然后报错

def test01(n):
    print("test01:",n)
    if n == 0:
        print("over")
    else:
        test01(n-1)

    print("test01***",n)

def test02():
    print("test02")

test01(4)

#递归小练习:计算阶乘
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

result = factorial(5)
print(result)