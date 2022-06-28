# -*- coding:utf-8 -*-
# @Time    : 2022/6/24 21:16
# @File    : _process_1.py
# Author: lee


# 案例一
# windows 下开启子进程，子进程代码通过 import 导入到子进程中

import os
import time
from multiprocessing import Process, cpu_count


# py文件就是一个子进程

def func(i, ind):
    # 子进程中 返回值 到不了 父进程
    print('%d start' % ind)
    print(os.getpid())
    time.sleep(i)
    print('%d end' % ind)



# 面向对象的方式实现多进程
class Myprocess(Process):

    def __init__(self, ind):
        # 多进程传递参数
        super().__init__()
        self.ind = ind

    def run(self):
        # 子进程执行的代码写在 run 中
        print('面向对象实现多进程 %d %d' % (self.ind, os.getpid()))



# 父进程 if 内
if __name__ == '__main__':
    print(os.getpid())

    # 进程中开启一个子进程
    # 子进程 p1 p2

    p1 = Process(target=func, args=(1, 1))
    p2 = Process(target=func, args=(1, 2))
    # p1.start()
    # p2.start()

    # 面向对象的方式开启子进程
    _p = Myprocess(1)
    _p.start()


# 二、进程的进阶
    # terminate() # 杀死子进程

    # is_alive()

    p3 = Process(target=func, args=(1, 3))

    # start() 为启动一个进程，此时进程处于就绪的状态，并没有运行
    # 等到进程分享到  CPU 的时间片，此时进程开始运行
    p3.start()

    print(p3.is_alive())


    # 杀死子进程
    # 不等待这一步的执行结果，父进程中向下执行
    p3.terminate() # 异步非阻塞

    print(p3.is_alive())
    time.sleep(2)
    print(p3.is_alive())
    print(p3.name)
    print(p3.pid)



    """
    1.join() # 主进程中存在 子线程.join(),
    则主进程会在子进程执行完毕之前被阻塞
    
    2.join() 相当于确保子进程结束
    
    3.主进程有join，主进程下面的代码一律不执行，直到进程执行完毕之后，再执行。
    
    """