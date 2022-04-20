# coding=utf-8
# 测试try...except...finally结构

try:
    f = open("d:/a.txt", "r")
    content = f.readline()
    print(content)
except:
    print("文件未找到")
finally:
    print("run in finally.关闭资源")
    try:
        f.close()
    except BaseException as e:
        print(e)
print("程序执行结束！")








