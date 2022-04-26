# 文本文件的读取

with open(r"e.txt", "r", encoding="utf-8") as f:
    str = f.read()
    print(str)

print("**********************************************")

with open(r"e.txt", "r", encoding="utf-8") as f:
    for a in f:
        print(a, end='')

print("**********************************************")

with open(r"e.txt", "r", encoding="utf-8") as f:
    while True:
        fragment = f.readline()
        if not fragment:
            break
        else:
            print(fragment, end='')