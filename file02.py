# 使用异常机制管理文件对象的关闭操作

try:
    f = open(r"my01.txt", "a")
    str = "chenweijie"
    f.write(str)
except BaseException as e:
    print(e)
finally:
    f.close()