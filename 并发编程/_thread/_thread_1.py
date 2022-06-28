# -*- coding:utf-8 -*-
# @Time    : 2022/6/24 21:50
# @File    : _thread_1.py
# Author: lee

# 一、线程

"""
线程：
    进程中的单位 --- 轻量级进程 相较进程效率更高
    1.单位级别：计算机被调度的最小单位
    2.线程之间没有数据隔离，同一个进程内的线程共享同一部分数据
    2.使用场景：
        开启、关闭、切换进程需要时间，过多的进程会导致电脑崩溃


"""


# 对比 线程与进程 的数据隔离

import os
import time
from threading import Thread, current_thread, enumerate
from multiprocessing import Process

tn = 0
pn = 0

def thread_func():
    global tn
    print('子线程start')
    tn += 1
    print(current_thread())
    print('子线程end')

join_lis = []
for i in range(100):
    t = Thread(target=thread_func)
    t.start()
    join_lis.append(t)

print(enumerate())

for t in join_lis:
    t.join()

print('tn:', tn) # >>> 数据不隔离，且效率很高



# def process_func():
#     global pn
#     print('子进程start')
#     pn += 1
#     print('子进程end')
#
#
# if __name__ == '__main__':
#     join_lis1 = []
#     for i in range(100):
#         p = Process(target=process_func)
#         p.start()
#         join_lis1.append(p)
#
#     for p in join_lis1:
#         p.join()
#
#     print('pn', pn) # >>> 0 数据隔离，且效率很低
#





# 二、线程中的方法

from threading import current_thread, active_count, enumerate


"""
1.current_thread()
        # 返回当前线程变量，<名字id，主进程id>
        <Thread(Thread-99, started 38032)>

    t = current_thread()
    t.ident 获得线程id


2.active_count()
        # 返回当前进程中的线程个数

3.线程中没有 terminate() 不可执行强制结束
        # why: 所有子线程都会在执行完所有任务之后门自动结束
         
         
4.enumerate()
        # 返回一个存储线程对象的列表
[<_MainThread(MainThread, started 39376)>, <Thread(Thread-100, started 38212)>]
<Thread(Thread-100, started 38212)>

    active_count() == len(enumerate())


"""



