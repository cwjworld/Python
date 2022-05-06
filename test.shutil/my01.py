# coding=utf-8
# 测试shutil模块的用法：拷贝、压缩

import shutil

# shutil.copyfile("1.txt", "1_copy.txt")

# shutil.copytree("movie/港台", "电影")

shutil.copytree("movie/港台", "电影2", ignore=shutil.ignore_patterns("*.txt"))