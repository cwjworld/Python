# enumerate函数和推导式生成列表

# a = ["我 love u!\n", "比特\n", "程序员\n"]
# b = enumerate(a)   # 把每一个元素都和索引关联起来，并且使用元组包含起来
# print(a)
# print(list(b))


with open("e.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    lines = [line.rstrip()+" #" + str(index)+"\n" for index, line in enumerate(lines)]

with open("e.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)