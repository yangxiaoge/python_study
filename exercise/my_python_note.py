__author__ = 'yjn'


# 学习Python
# 廖雪峰教程:
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431608990315a01b575e2ab041168ff0df194698afac000

def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


print(power(5))
print(power(5, 3))

print('------------------------------------')


def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)


enroll('haha', '11')

print('------------------------------------')


def add_end(list=None):
    if list is None:
        list = []
        list.append("END")
    return list


add_end([1, 2, 3])

print('------------------------------------')


# 定义一个递归函数
# 计算阶乘 n! = 1 x 2 x 3 x ... x n
# fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(1))
print(fact(5))
print(fact(10))
# print(fact(5000)) 栈溢出
print('------------------------------------')


# ------------------------------------高级特性----------------------------------------- #

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317568446245b3e1c8837414168bcd2d485e553779e000
# 掌握了Python的数据类型、语句和函数，基本上就可以编写出很多有用的程序了。
# 比如构造一个1, 3, 5, 7, ..., 99的列表，可以通过循环实现：
# 在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。
# 基于这一思想，我们来介绍Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。
print('高级特性')
L = []
n = 1
while n <= 99:
    L.append(n)
    n += 2;
print(L)  # 打印出list

print('------------------------------------')

# 切片
# 取出list L 前N个元素
print('切片')
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作
# 对应上面的问题，取前3个元素，用一行代码就可以完成切片：
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print(L[0:3])
print(L[1:3])
print(L[-2:])  # 既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print(L[-2:-1])  # 记住倒数第一个元素的索引是-1
print('------------------------------------')

# 切片操作十分有用。我们先创建一个0-99的数列：
L = list(range(100))
print(L)
print(L[10:20])  # 前11-20个数：
print(L[:10:2])  # 前10个数，每两个取一个：
print(L[::2])  # 所有数，每5个取一个：
print(L[::])  # 甚至什么都不写，只写[:]就可以原样复制一个list：
print('------------------------------------')

# tuple 也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])  # 前3个字符
print('ABCDEFG'[::2])  # 所有字符，每2个取一个：
print('------------------------------------')

# 迭代
print('迭代')
d = {'a': 1, 'b': 2, 'c': 3}
for i in d:
    print(i)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable

print(isinstance("234235", Iterable))  # str是否可迭代 True
print(isinstance([1, 2, 3], Iterable))  # list是否可迭代 True
print(isinstance(123, Iterable))  # 整数是否可迭代  False

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成 索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in ([(1, 1), (2, 4), (6, 8)]):
    print(x, y)
print('------------------------------------')

# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
print(list(range(1, 11)))
print([x * x for x in range(1, 11) if x % 2 == 0])

import os  # 导入os模块

print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录
print('------------------------------------')
L1 = ['Hello', 'World', 18, 'Apple', None]  # list中既包含字符串，又包含整数 ,只取出字符串类型的
L2 = []
print('方法一')
# 方法一
for k in L1:
    if (isinstance(k, str)):  # 使用内建的isinstance函数可以判断一个变量是不是字符串：
        L2.append(k.lower())  # lower() 字符串转小写
print(L2)
print('方法二')
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

print('-----------------以下来自: http://www.sololearn.com/Play/Python --------------------------------')
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])

print('List Comprehensions------------------------------------')
# a list comprehension
cubes = [i**3 for i in range(5)] # 两个 * 代表 冥次方
print(cubes)
nums = [i*2 for i in range(10)] # 一个 * 代表乘号
print(nums)

# A list comprehension can also contain an if statement to enforce a condition on values in the list.
# Example:
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)
