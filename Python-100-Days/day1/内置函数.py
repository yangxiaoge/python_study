# -*- coding: utf-8 -*-
"""
Python 的内置函数
	- 数学相关: abs / divmod / pow / round / min / max / sum
	- 序列相关: len / range / next / filter / map / sorted / slice / reversed
	- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
	- 数据结构: dict / list / set / tuple
	- 其他函数: all / any / id / input / open / print / type
"""


# 定义一个函数
def testFilter(params):
    return len(params) == 5  # 过滤掉长度不为5的


print(chr(0x6768))
print(hex(ord('杨')))
print(abs(-10000))
print(round(-2.1))
print(pow(2, 3))

fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)])  # slice(1, 3) start -- 起始位置,stop -- 结束位置,左闭右开

fruits2 = list(filter(testFilter, fruits))
print(fruits)
print(fruits2)
