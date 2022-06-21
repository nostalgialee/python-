# -*- coding:utf-8 -*-
# @Time    : 2022/6/20 13:42
# @File    : __init__.py
# Author: lee



"""
yield 与 yield from
实现的协程
"""


# 一、前言

def gen():
    for i in "AB":
        yield i
    for i in range(1, 3):
        yield i

g = gen()




"""
yield from 是 python3.3 引入的新语法，主要用于解决在生成器中不方便
使用生成器的问题

    功能1
        让嵌套的生成器不再通过循环迭代，而直接使用 yield from
    
"""

# 功能1
titles = ['Python', 'Java', 'C++']

def func1(titles):
    yield titles


def func2(titles):
    yield from titles


# for title in func1(titles):
#     print(title)

# ['Python', 'Java', 'C++']
# yield返回的完整的titles列表，

# for title in func2(titles):
#     print(title)
# Python
# Java
# C++
# yield from返回的是列表中的具体元素。
# yield from可以看作是
# for title in titles:
#   yield title
#
# 这样就可以用yield from减少了一次循环。


"""
    功能2
        打开双向通道，把最外层给调用方与最内层的子生成器链接起来，
        二者可以直接通信。
        
    例子 通过生成器实现整数相加，通过 send() 函数向生成器中传入加数，
     最后传入None结束相加。total保存结果。
     
     由此:
     x = yield from a() # x表示的是生成器a()的返回值
     x = yield          # x表示的是send()传入的值
     
     
     通过委托生成器，与子生成器来实现
"""

def generation1():
    """
    子生成器

    :return:
    """
    total = 0
    while 1:
        x = yield # 管道接受 send() 发来的值
        print('x:', x)
        if not x:
            break
        total += x
    return total

def generation2():
    """
    委派生成器

    g2是调用generator_2()
    得到的生成器对象，作为协程使用。

    :return:
    """

    while True:
        total = yield from generation1()
        print('total:', total)



if __name__ == "__main__":
    g2 = generation2()
    g2.send(None) # 激活生成器
    g2.send(2)				# 解释6
    g2.send(3)
    g2.send(None)			# 解释7







# yield from
def gen():
    yield subgen1()
    yield subgen2()


def subgen1():
    for i in "AB":
        yield i


def subgen2():
    for i in range(1, 3):
        yield i



"""
yield 与 yield from 关键字必须写在函数体内，
含有 yield from 关键字的生成器成为委派生成器


yield from 会把执行权交给其后面的生成器参数，
    yield from 子生成器A
    
当子生成器抛出 Stopiteration 执行权回到委派生成器内部

def generation():
    yield from son_generation()


def son_generation()
    for i in range(10):
        yield i
    
"""
# yield from 例子
from .yield_from_example import *



