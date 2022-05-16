# import a.aa.module_AA
# a.aa.module_AA.fun_AA()

# from a.aa import module_AA
# module_AA.fun_AA()

# from a.aa.module_AA import fun_AA
# fun_AA()

import a
import math

print(a.math.pi)
print(id(math))
print(id(a.math))