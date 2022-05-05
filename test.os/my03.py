# coding=utf-8
# 测试os.path中关于目录、路径的操作

import os
import os.path

# 判断：绝对路径、是否目录、是否文件、是否存在
print(os.path.isabs("d:/a.txt"))
print(os.path.isdir("d:/a.txt"))
print(os.path.isfile("d:/a.txt"))
print(os.path.exists("d:/a.txt"))

# 获得文件的基本信息
print(os.path.getsize("d:/a.txt"))
print(os.path.abspath("d:/a.txt"))
print(os.path.dirname("d:/a.txt"))

print(os.path.getctime("d:/a.txt"))
print(os.path.getatime("d:/a.txt"))
print(os.path.getmtime("d:/a.txt"))

# 对路径的操作
path = os.path.abspath("b.txt")
print(os.path.split(path))
print(os.path.splitext(path))

print(os.path.join("aa", "bb", "cc"))