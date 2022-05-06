# coding=utf-8
# 测试walk遍历

import os

all_files = []
path = os.getcwd()
list_files = os.walk(path)

for dirpath, dirnames, filenames in list_files:
    for dir in dirnames:
        all_files.append(os.path.join(dirpath, dir))
    for file in filenames:
        all_files.append(os.path.join(dirpath, file))

for file in all_files:
    print(file)

