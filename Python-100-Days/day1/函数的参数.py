# -*- coding: utf-8 -*-
"""
 函数的参数
	- 默认参数
	- 可变参数
	- 关键字参数
	- 命名关键字参数
"""


# 参数默认值
import math


def f1(a, b=5, c=10):
    return a + b * 2 + c * 3


print(f1(1, 2, 3))
print(f1(100, 200))
print(f1(100))
print(f1(c=2, b=3, a=1))


# 可变参数
def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())


# 关键字参数
def f3(**kw):
    if 'name' in kw:
        print('欢迎你 %s!' % kw['name'])
    elif 'tel' in kw:
        print('你的联系电话是: %s!' % kw['tel'])
    else:
        print('没找到你的个人信息!')


param = {'name': '羊羊羊', 'age': 38}
f3(**param)
print()
f3(name='羊羊羊', age=18, tel='199xxxxxxxx')
f3(user='羊羊羊', age=18, tel='199xxxxxxxx')
f3(user='羊羊羊', age=18, mobile='199xxxxxxxx')

# 阶乘
print(math.factorial(5))