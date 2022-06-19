# -*- coding:utf-8 -*-
# @Time    : 2022/6/18 21:45
# @File    : derectors.py
# Author: lee


# 装饰器相关


# 一、functools.wraps 相关

def tracer(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r,%r)->%r' % (func.__name__, args, kwargs, result))
        return result
    return wrapper

# 被装饰函数
@tracer
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
# fibonacci((1,),{})->1
# fibonacci((0,),{})->0
# fibonacci((2,),{})->1
# fibonacci((1,),{})->1
# fibonacci((3,),{})->2
print(fibonacci)
# <function tracer.<locals>.wrapper at 0x000001E2FF090950>
print('help:') # help:
help(fibonacci)
# Help on function wrapper in module __main__:
# wrapper(*args, **kwargs)


"""

装饰器完全可以正常工作。。。
但是，函数的名字变成装饰器中的包装器了！！！help内置函数也失效了
也就是说，原函数的属性失效了
如果想要保留原函数的属性，就可以用到functools.wraps了

"""




from functools import wraps


def tracer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r,%r)->%r' % (func.__name__, args, kwargs, result))
        return result
    return wrapper

# 被装饰函数
@tracer
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
# fibonacci((1,),{})->1
# fibonacci((0,),{})->0
# fibonacci((2,),{})->1
# fibonacci((1,),{})->1
# fibonacci((3,),{})->2
print(fibonacci)
# <function fibonacci at 0x0000023B11F609D8>
print('help:') # help:
help(fibonacci)
# Help on function fibonacci in module __main__:
# fibonacci(n)



# 二、多个装饰器执行顺序

def war1(func):
    print('war1')
    def inner(*args, **kwargs):
        print('=======war1 start=======')
        func(*args, **kwargs)
        print('=======war1 end=======')
    return inner


def war2(func):
    print('war2')
    def inner(*args, **kwargs):
        print('=======war2 start=======')
        func(*args, **kwargs)
        print('=======war2 end=======')
    return inner

@war1
@war2
def func():
    print('func runs')


func()


"""
装饰器函数的执行顺序：
    被装饰函数的定义阶段
    被装饰函数的执行阶段
    装饰器函数在被装饰函数定义好后立刻执行
    
        函数定义阶段：执行顺序从最靠近函数的装饰器开始，自内而外的执行
        函数执行阶段：执行顺序由外而内，一层层执行
    
"""

# 1. 当被装饰函数，被定义 而 未被执行的时候，装饰器函数开始执行
# @war1
# @war2
# def func():
#     print('func runs')

# func = war1(func)
# func = war2(func)



"""

被装饰函数定义阶段：
    例子中：
    先走 war2
    后走 war1
war1(war2(func))

war2(f) 作为被装饰函数 放入 war1 中

内部 inner 中的伪代码
    def inner_b(*args, **kwargs):
        print('=======war1 start=======')
        war2(func)
        print('=======war1 end=======')

被装饰函数执行阶段：
    例子中 
    先走 b
    后走 a

打印结果：


'war2'
'war1'
'=======war1 start======='
'=======war2 start======='
'func runs'
'=======war2 end======='
'=======war1 end======='


"""

