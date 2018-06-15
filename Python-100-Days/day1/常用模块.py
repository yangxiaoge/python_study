# -*- coding: utf-8 -*-
"""
Python 常用模块
	- 运行时服务相关模块: copy / pickle / sys / ...
	- 数学相关模块: decimal / math / random / ...
	- 字符串处理模块: codecs / re / ...
	- 文件处理相关模块: shutil / gzip / ...
	- 操作系统服务相关模块: datetime / os / time / logging / io / ...
	- 进程和线程相关模块: multiprocessing / threading / queue
	- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
	- Web 编程相关模块: cgi / webbrowser
	- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...
"""
import os
import shutil
import time

seconds = time.time()
print(seconds)

# 转换成本地时间格式
localtime = time.localtime(seconds)
print(localtime)
print('%d年%d月%d日' % (localtime.tm_year, localtime.tm_mon, localtime.tm_mday))

asctime = time.asctime(localtime)
print(asctime)

strftime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strftime)
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)

# 拷贝文件内容
shutil.copy('D:\yangjianan\github\python_study\Python-100-Days\day1\算法\九九乘法口诀.py',
            'D:\yangjianan\github\python_study\Python-100-Days\day1\est.py')
os.system('ls -l')

# 进入目录
os.chdir('D:\yangjianan\github\python_study\Python-100-Days\day1\yang')
os.system('ls -l')
# 创建文件夹
os.mkdir('test')
