#测试推导式

#列表推导式
y = [x*2 for x in range(1,50) if x%5==0]
print(y)

cells = [(row,col) for row in range(1,10) for col in range(1,10)]
print(cells)

print("*******************************************************")

#字典推导式
#统计文本中各个字符出现的次数
my_text = 'i love you,i love sxt, i love zj'
char_count = {c:my_text.count(c) for c in (my_text)}
print(char_count)

print("*******************************************************")

#集合推导式
b = {x for x in range(1,100) if x%9==0}
print(b)

print("*******************************************************")

#生成器推导式
gnt = (x for x in range(4))
#print(tuple(gnt))

for x in gnt:  #gnt是s生成器对象，生成器是可迭代对象,只能使用一次
    print(x,end=',')
print(tuple(gnt))
