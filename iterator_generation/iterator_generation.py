# -*- coding:utf-8 -*-
# @Time    : 2022/6/19 22:52
# @File    : iterator_generation.py
# Author: lee

# 一、迭代器
"""
python协议：
    具有 __iter__ 方法的对象 --- 可迭代对象
    对象.__iter__() 可以创建一个迭代器

    具有 __iter__() 与 __next__()的即为迭代器


迭代器的特点：
    1.惰性机制
    2.不能从下向上
    3.一次性取完便无
    4.省内存
"""

class _List:

    def __init__(self, iterable):
        self.l = iterable

    def __iter__(self):
        # import copy
        # return copy.deepcopy(self)
        return self

    def __next__(self):
        if self.l:
            return self.l.pop(0)
        else:
            raise StopIteration

l = [1,2,4,5,6,7,8]

a = iter(l) # 内部方法 __iter__() 被调用
            # 创建一个 迭代器, 怀疑这里是有用到深拷贝
b = iter(l)
# a, b 两个不同的迭代器

# print(next(a)) # 1
# print(next(b)) # 1





# 二、生成器
"""
本质：迭代器

优点：
    1.延迟加载：对于处理长序列问题，更加节省存储空间，
    即生成器每次在内存中只存储一个值

"""
def func():
    n = 0
    while 1:
        n += 1
        tmp = yield n
        print(tmp)

g = func()
g1 = func()
# print(g.__next__())
# 1 ---> print(1)
# 5 ---> yield 5

# 生成器地址的打印
print(func) # <function func at 0x000002292A1147B8>
print(func()) # <generator object func at 0x000002293A96A200>



# send 方法： 将内容发送至 yield n 语句
# tmp = yield n # 发送者 tmp
"""
生成器状态在GEN_SUSPENDED时，通过send方法向生成器传递值，
生成器必须预激活，next(gen)或者gen.send(None)都可以用于预激活，
如果不激活直接传递非None值，解释器会直接报错。
"""
res = g1.send(None)
print(res) # 你的值

res1 = g1.send('起点')
# 不打印none 是因为 send 直接执行了 tmp = yield n
# 将 tmp 赋值为 起点
print(res1)

# 1
# 起点
# 2



def task1(n):
    for i in range(n):
        print("正在执行搬第%d砖" % n)
        yield n


def task2(n):
    for i in range(n):
        print("正在听第%d歌" % n)
        yield n



g1 = task1(10)
g2 = task2(5)
while True:
    try:
        g1.__next__()
        g2.__next__()
    except StopIteration:
        break




"""
throw()
向生成器抛出一个异常，如果生产期内部不处理这个异常，
异常会上浮到客户端代码，如果客户端代码不捕获这个异常，那么会直接报错


close()
给生成器一个停止停止。
"""

# yield 例子
# from  .generation_example.yield_example import *











































