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

print(next(a)) # 1
print(next(b)) # 1



# 二、生成器


































