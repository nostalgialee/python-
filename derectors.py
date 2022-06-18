# -*- coding:utf-8 -*-
# @Time    : 2022/6/18 21:45
# @File    : derectors.py
# Author: lee


# 装饰器相关

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
