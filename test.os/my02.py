# coding=utf-8
# 测试os模块中，关于文件和目录的操作

import os

# 获取文件和文件夹相关的信息
print(os.name)   # windows-->nt     linux 和 unix-->posix
print(os.sep)    # windows-->\      linux 和 unix-->/
print(repr(os.linesep))     # windows-->\r\n     linux-->\n\

print(os.stat("my02.py"))

# 关于工作目录的操作
# print(os.getcwd())
# os.chdir("d:")  # 可以改变工作目录
# os.mkdir("书籍")

# 创建目录、多级目录、删除
# os.mkdir("书籍")
# os.rmdir("书籍")  # 相对路径都是相对于当前的工作目录

# os.makedirs("电影/港台/周星驰")
# os.removedirs("电影/港台/周星驰")      # 只能删除空目录
# os.makedirs("../音乐/港台/刘德华")     # ../指的是上一级目录
# os.removedirs("../音乐/港台/刘德华")

# os.rename("电影", "movie")
dirs = os.listdir("movie")
print(dirs)
