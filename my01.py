# 异常结构try_exception
# coding=utf-8
print("step0")
try:
    print("step1")
    a = 3/0
    print("step2")
except BaseException as e:
    print("step3")
    print(e)
    print(type(e))

print("end!!!")


print("---------------------------------------")

# 示例：循环输入数字，如果不是数字则异常处理，知道输入88，则结束循环。
while True:
    try:
        x = int(input("请输入一个数字："))
        print("输入的数字：", x)
        if x == 88:
            print("退出程序")
            break
    except BaseException as e:
        print(e)
        print("异常，输入的不是一个数字")

print("循环数字输入程序结束!")