#测试参数的传递
#传递可变对象

a = [10,20]

print(id(a))
print(a)

print("****************************************")

def test01(m):
    print(id(m))
    m.append(300)
    print(id(m))

test01(a)
print(a)

print("****************************************")

