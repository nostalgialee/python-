# -*- coding:utf-8 -*-
# @Time    : 2022/6/27 13:27
# @File    : _process_4.py
# Author: lee


# 进程池

"""

与进程池类似,
线程池是在系统启动时就先创建大量空闲的线程,
程序提交一个任务给线程池, 线程池便会调用一个线程来执行该任务,
当任务运行完毕后, 该线程并不会关闭,
而是返回到线程池中再次变为空闲状态等待下一个提交的任

"""




import time
from multiprocessing import Process, cpu_count
from concurrent.futures import ProcessPoolExecutor


"""
concurrent.futures模块，(after python 3.2)
    提供了:
    
        ProcessPoolExecutor # 实现了对multiprocessing 更高级的抽象

        ThreadPoolExecutor # 实现了对threading 更高级的抽象，

        Executor --- 一个抽象类，
            它不能被直接使用。它为具体的异步执行定义了一些基本的方法。 
            ThreadPoolExecutor和ProcessPoolExecutor继承了Executor，
        
        
        Executor 中有 __enter__/__exit__ 方法，所以池对象可以使用 with 语句
        

"""

# 池类的常用方法

def wort_func(x):
    time.sleep(1)
    print(x)
    return x


def callback(args):
    # args: future 实例对象
    print('回调函数中的任务返回值', args.result())
    print('这里是回调函数')


if __name__ == "__main__":

    process_pool = ProcessPoolExecutor(3)
    # 以核心数规定进程池的数量, 默认以cpu数量或者1个

    f1 = process_pool.submit(wort_func, 'sam') # 提交一个任务
    f2 = process_pool.submit(wort_func, 'tom') # 提交一个任务
    # 返回任务的结果。f1 f2 Future 实例

    """
    Future: 池对象.submit() 后的返回值
    
        # Future可以理解为一个在未来完成的操作,这是异步编程的基础
    
        obj.add_done_callback() # 增加回调函数
        obj.result() # 获得进程执行结果
        
        
    """

    f1.add_done_callback(callback)
    f2.add_done_callback(callback)

    print("主进程代码执行完毕")








    # map --- 可以保证输出的时候有序
    """
    map(func,*iterables,timeout=None,chunksize=1)
    返回一个map(func, *iterables)迭代器，
    迭代器中的回调执行返回的结果有序的
    
    ret = process_pool.map(wort_func, ['a','b','c'])
    # 循环得到结果
    for i in ret:
        print(ret)
    
    """



    # shutdown 释放系统资源
    # 在Executor.submit()或 Executor.map()等异步操作后调用
    # 这里我们使用with操作符，使得当任务执行完成之后，
    # 自动执行shutdown函数，而无需编写相关释放代码。





# 记得回来看源码
# 知乎上的精彩问答
# https://zhuanlan.zhihu.com/p/438627177

