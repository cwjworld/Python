# coding=utf-8
# 测试trackback模块的使用

import traceback
#######将异常信息输出到指定的文件夹中#######
try:
    print("step1")
    num = 1/0
except:
    with open("d:/a.txt", "a") as f:
        traceback.print_exc(file = f)




