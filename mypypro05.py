#测试嵌套循环
for x in range(5):
    for y in range(5):
        print(x, end="\t")
    print()#本身就有换行的含义

print("****************************************************")

#打印九九乘法表
for m in range(1, 10):
    for n in range(1, m+1):
        print("{0} * {1} = {2}".format(m, n, (m*n)), end='\t')
    print()

print("****************************************************")

#使用列表和字典存储表格的数据
r1 = dict(name="陈伟杰", age=18, salary=30000, city="北京")
r2 = dict(name="陈伟杰", age=18, salary=30000, city="上海")
r3 = dict(name="陈伟杰", age=18, salary=30000, city="深圳")
tb = [r1, r2, r3]

for x in tb:
    if x.get("salary") > 15000:
        print(x)
