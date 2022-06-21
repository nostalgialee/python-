# -*- coding:utf-8 -*-
# @Time    : 2022/6/21 13:50
# @File    : yield_example.py
# Author: lee


import inspect
from functools import wraps


"""
功能描述：
    待机持续输入数字，累计计算所有值的 数字总个数，总值，平均值
"""





def prime_generator(func):
    """
    预激活生成器的装饰器
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        # next(gen)
        gen.send(None)
        return gen

    return wrapper


@prime_generator
def average():
    """
    生成器函数
    :return:
    """
    count = 0
    total = 0
    avg = 0
    while True:
        try:
            x = yield count, total, avg
        except ValueError:
            print("输入的值不符合要求")
            continue
        if x == None:
            # break
            continue
        count += 1
        total += x
        avg = total / count


def client():
    """
    客户端代码
    :return:
    """
    avg = average()  # 创建生成器对象
    print(inspect.getgeneratorstate(avg))  # GEN_CREATED
    # s1 = next(avg) # 预激活生成器，生成器能运行，运行到第一个yield进入等待状态 ， avg.send(None) 等同于 next(avg)
    # print(s1)
    while True:
        x = input("请输入值：")
        if x == "q":
            break
        try:
            x = float(x)
            res = avg.send(x)
            # 在生成器内部需要提前激活生成器 --- 装饰器实现

            print(f"count:{res[0]},total:{res[1]},avg:{res[2]}")
        except ValueError:
            avg.throw(ValueError)
        print(inspect.getgeneratorstate(avg))  # GEN_SUSPENDED

    avg.close()
    print(inspect.getgeneratorstate(avg))  # GEN_CLOSED


if __name__ == '__main__':
    client()
