# seek()任意位置操作
with open("e.txt", "r", encoding="utf-8") as f:
    print("文件名是：{0}".format(f.name))
    print(f.tell())
    print("读取的内容：{0}".format(str(f.readline())))
    print(f.tell())
    f.seek(0)
    print("读取的内容：{0}".format(str(f.readline())))