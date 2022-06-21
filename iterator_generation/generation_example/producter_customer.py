# -*- coding:utf-8 -*-
# @Time    : 2022/6/21 15:01
# @File    : producter_customer.py
# Author: lee


import time

def customer():
    while 1:
        i = yield
        print(f"消费者消费了{i}")


def productor(c):
    c.send(None)
    for i in range(1,10):
        print(f"生产者生产了{i}")
        c.send(i)
        time.sleep(1)


if __name__ == '__main__':
    c = customer()
    productor(c)
