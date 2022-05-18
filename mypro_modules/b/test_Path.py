# 测试sys.path的用法。测试模块搜索路径

import sys
sys.path.append("d:/")    # 临时添加目录
print(sys.path)
