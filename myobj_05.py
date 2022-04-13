# 测试方法的动态性

class Person:

    def work(self):
        print("努力上班!")


def play_game(s):
    print("{0}在玩游戏".format(s))

def work2(s):
    print("好好工作，努力上班!")


Person.play = play_game;
p = Person()
p.work()
p.play()    # Person.play(p)

Person.work = work2

p.work()