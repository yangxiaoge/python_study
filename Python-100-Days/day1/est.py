# -*- coding: utf-8 -*-
"""
 输出乘法口诀表 (九九表)
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d×%d=%d' % (j, i, i * j), end='\t')  # '\t'制表符
    print('')  # 换行
