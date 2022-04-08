#传递不可变对象时，如果发生拷贝，是浅拷贝

a = (10,20,[5,6])
print("a:",id(a))

def test01(m):
    print("m:", id(m))
    m[2][0] = 888
    print(m)
    print("m:", id(m))

test01(a)
print(a)