__author__ = 'yjn'
# -*- coding: utf-8 -*-

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
cubes = [i ** 3 for i in range(5)]  # 两个 * 代表 冥次方
print(cubes)
nums = [i * 2 for i in range(10)]  # 一个 * 代表乘号
print(nums)

# A list comprehension can also contain an if statement to enforce a condition on values in the list.
# Example:
evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(evens)

print("{c}, {b}, {a}".format(a=5, b=9, c=7))

print('继续廖雪峰的教程------------------------------------')
# 生成器
g = (x * x for x in range(10))
# for 循环打印
for gg in g:
    print('生成器:' + format(gg))


# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 下面定义一个fib函数
print('函数定义 斐波拉契数列')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

# 上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
print('generator定义 斐波拉契数列')


def g_fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for g in g_fib(6):
    print(g)

print('练习: 杨辉三角')


def triangles(rowNumber):
    nowRow = 1
    row = [1]
    while nowRow <= rowNumber:
        yield row
        newPart = [1] + [row[i]+row[i+1] for i in range(len(row)-1)] + [1]
        row = newPart[:]
        nowRow += 1
for t in triangles(10):
    print(t)

print('迭代器------------------------------------')
#迭代器
"""
我们已经知道，可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象：
"""
print("判断 可迭代对象：Iterable-------------------")
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('haha',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(1000,Iterable))

"""
而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
可以使用isinstance()判断一个对象是否是Iterator对象：
"""
print("判断 对象称为迭代器：Iterator----------------")
from collections import Iterator
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('haha',Iterator))
print(isinstance((x for x in range(10)),Iterator))
print(isinstance(1000,Iterator))

"""
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
把list、dict、str等Iterable变成Iterator可以使用iter()函数：
"""
print('把Iterable变成Iterator---------------------')
print(isinstance(iter([]),Iterator))

"""
小结

凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass
"""

# 高阶函数
"""
高阶函数英文叫Higher-order function。什么是高阶函数？我们以实际代码为例子，一步一步深入概念。

变量可以指向函数
以Python内置的求绝对值的函数abs()为例，调用该函数用以下代码：
"""
print('高阶函数---------------------')
print(abs(-10))

#如果一个变量指向了一个函数，那么，可否通过该变量来调用这个函数？用代码验证一下：
f = abs
print(f(-10))

def add(x,y,abs):
    return f(x)+f(y)
print(add(5,6,abs))

#map/reduce
"""
Python内建了map()和reduce()函数。

如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，你就能大概明白map/reduce的概念。
我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
"""
print('map/reduce 函数----------------')
def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6])
print(list(r))

"""
map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，
还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
"""
print(list(map(str, [1,2,3,4,5,6])))

"""
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""
# 比方说对一个序列求和，就可以用reduce实现：
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,2,3,4,5,6])) # 当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。

# 如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn(x,y):
    return x*10+y

print(reduce(fn,[1, 3, 5, 7, 9]))

# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn, map(char2num, '13579')))

# 整理成一个str2int的函数就是：
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
# 还可以用lambda函数进一步简化成：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int_2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int_2('32135161123'))

# 测试:
def normalize(name):
    return name.capitalize() # str.capitalize() 首字母大写
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 把字符串'123.456'转换成浮点数123.456：
from functools import reduce
def str2float(s):
    s = s.split('.')
    def f1(x,y):
        return x*10+y
    def f2(x,y):
        return x/10+y
    def str2Num(str):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[str]
    return reduce(f1,map(str2Num,s[0])) + reduce(f2,list(map(str2Num,s[1]))[::-1])/10 # [::-1]翻转list

print('str2float(\'123.456\') =', str2float('123.456'))

# filter
"""
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。
例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
"""
print('filter------------------------------------')

def isOddNum(s):
    return s%2==1
print(list(filter(isOddNum,[1,2,3,4,5,6,7,8,9,10])))
# 结果: [1, 5, 9, 15]

# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A', '', 'B', None, 'C', '  '])))
# 结果: ['A', 'B', 'C']

# 用filter求素数
def _odd_iter(): # 注意这是一个生成器，并且是一个无限序列。
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n): # 然后定义一个筛选函数：
    return lambda x: x % n > 0

def primes(): #最后，定义一个生成器，不断返回下一个素数：
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():# 打印1000以内的素数:
    if n < 1000:
        print('素数 ',n)
    else:
        break

#练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
# 其实素数, 相当于 正过来反过来相等
def is_palindrome(n):
    return n == int(str(n)[::-1]) # 知识点:str[::-1], 字符串反转,注意:如果转换成字符, 收尾有0时会判断错误, 应该再转换为int, 做比较
output = filter(is_palindrome, range(1, 1000))
print(list(output))

# sorted 排序算法
"""
排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，
但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
"""
print('sorted 排序算法---------------------------')
# Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21],key=abs))


L = ['bob', 'about', 'Zoo', 'Credit']
print('排序前:',sorted(L))
print('排序后:',sorted(L, key=str.lower))

# 练习
"""
假设我们用一组tuple表示学生名字和成绩：
请用sorted()对上述列表分别按名字排序:
"""
print('按照名字排序--------------------')
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
  return t[0].lower and t
print('排序前:',L)
print('排序后:',sorted(L, key=by_name))
"""
再按成绩从高到低排序：
"""
print('按照成绩排序--------------------')
def by_score(t):
    return t[1]
print(sorted(L,key = by_score))

# 返回函数
"""
函数作为返回值

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431835236741e42daf5af6514f1a8917b8aaadff31bf000
"""
print('返回函数--------------------')
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
print('求和:',calc_sum(1,32,4,51))

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9) #当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
print(f)
print(f())
'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
'''
# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2) # f1()和f2()的调用结果互不影响。
'''
返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''

# 匿名函数
"""
当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
"""
print('匿名函数--------------------')
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

'''
通过对比可以看出，匿名函数 lambda x: x * x 实际上就是：
def f(x):
    return x * x
'''
# 匿名函数也是一个函数对象，匿名函数也可以赋值给一个变量
f_lambda = lambda x:x * x
print(f_lambda(3))
# 同样，也可以把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda: x * x + y * y

# 装饰器(有点深度)
"""
由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000
"""
print('装饰器-------------------------------')
def now():
    print('2016-9-13 10:33:37')
f_now = now
f_now()
# 函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)
print(f_now.__name__)
'''
现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
'''
import functools
print('2层嵌套的decorator------')
def log(func):
    def wrap(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrap
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print('2016-9-13 10:48:04')
# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
now()
print('3层嵌套的decorator------')
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('DEBUG')
def now():
    print('2016-9-13 11:10:00')
now()

# 偏函数
"""
Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。
在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：
int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
"""
print('偏函数--------------------------------')
pint = int('13214')
print(pint)
# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print(int('12345',base=8)) # 转成八进制
print(int('12345',16)) # 转成十六进制

# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
def int2(x,base=2):
    return int(x,base)
