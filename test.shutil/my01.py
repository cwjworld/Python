# coding=utf-8
# 测试shutil模块的用法：拷贝、压缩

import shutil
import zipfile

# shutil.copyfile("1.txt", "1_copy.txt")

# shutil.copytree("movie/港台", "电影")

# shutil.copytree("movie/港台", "电影2", ignore=shutil.ignore_patterns("*.txt"))

# 压缩、解压缩
shutil.make_archive("电影/gg", "zip", "movie/港台")

z1 = zipfile.ZipFile("a.zip", "w")
z1.write("1.txt")
z1.write("1_copy.txt")
z1.close()

z2 = zipfile.ZipFile("a.zip", "r")
z2.extractall("电影")
z2.close()

