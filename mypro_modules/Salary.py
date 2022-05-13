# encoding=utf-8
# 模块化编程流程(设计与分离)
# 用于计算公司员工薪资
company = "西安比特"


def yearSalary(monthSalary):
    # 根据传入的月薪计算年薪  monthSalary*12
    return monthSalary*12


def daySalary(monthSalary):
    # 根据传入的月薪计算日薪 monthSalary/12
    return monthSalary/22.5


if __name__ == "__main__":
    print(yearSalary(5000))
