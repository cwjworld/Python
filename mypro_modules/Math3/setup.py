from distutils.core import setup

setup(
    name='SuperMath',   # 对外版本名字
    version='1.0',  # 版本号
    description='描述',   # 第一个对外发布的模板，里面只有数学方法，用于测试
    author='大卫',    # 作者
    author_email='564521556@qq.cpm',
    py_modules=['SuperMath.demo1', 'SuperMath.demo2']     # 要发布的模板
)