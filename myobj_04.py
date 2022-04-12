# 测试可调用方法__call__()

class SalaryAccount:
    '''工资计算类'''

    def __call__(self, salary):
        print("算工资啦...")
        yearSalary = salary*12
        daySalary = salary//22.5
        hourSalary = daySalary//8

        return dict(yearSalary=yearSalary, monthSaaty=salary, daySalary=daySalary, hourSalary=hourSalary)


s = SalaryAccount()
print(s(3000))
