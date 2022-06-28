# -*- coding:utf-8 -*-
# @Time    : 2022/6/25 11:29
# @File    : _process_3.py
# Author: lee



# 锁
#     应用场景：多个进程操作同一数据时，
#       可能会导致数据不安全，应当使用锁

from multiprocessing import Process, Lock, Queue

"""
一、

class Lock(object):
    def acquire(self, blocking=True, timeout=-1):
        # 上锁
        pass

    def release(self):
        # 开锁
        pass

# 相当于同步阻塞，join的作用


互斥锁：
    保证对于数据的修改操作
        在同一时刻多个进程只有一个进程在执行
    使用互斥锁的时候要注意死锁的情况
    

死锁：
    概念：同一进程之内，也有锁的竞争
    
    形成原因：
        1.同一进程之内相同的锁连续 acquire 会造成死锁
        2.锁没有释放
        3.多个进程加了多个锁，造成死锁
        
        
    后果：死锁一旦产生就会造成应用程序的停止响应，
        应用程序无法再继续往下执行了。

    ex: 一个死锁的例子

    
from multiprocessing import Process, Lock

l1 = Lock()
l2 = Lock()


class MyProcess(Process):

    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        l1.acquire()
        print('lock 1')
        l2.acquire() # step *
        print('lock 2')
        l2.release()
        l1.release()

    def func2(self):
        l2.acquire()
        print('lock 2')
        
        import time
        time.sleep(2)
        
        l1.acquire() # step #
        print('lock 1')

        l1.release()
        l2.release()

进程1 执行 func1()上锁--1,2 
                 解锁--2,1
                 

进程2执行func1 --上锁1


进程1 执行 func2() 上锁2，并进入休眠
进程2 由于进程1 上锁 2, 所以阻塞在 step *

进程1结束休眠之后，被阻塞在 step # --- 因为进程2已经为1上锁

造成死锁的现象


"""




# 二、基于进程队列传递数据

def son_process(q):
    data = q.get()
    print("data", data)


if __name__ == '__main__':
    q = Queue()
    q.put('主进程向子进程传递数据')
    p = Process(target=son_process, args=(q,))
    p.start()

# >>> data 主进程向子进程传递数据




# 三、生产者消费者模型


# 多进程写法
import time
import random

class Customer(Process):

    def __init__(self, q):
        super().__init__()
        self.q = q
        self.start()

    def run(self):
        while 1:
            item = self.q.get()
            print('customer do')


class Productor(Process):

    def __init__(self, q):
        super().__init__()
        self.q = q
        self.start()

    def run(self):
        while 1:
            time.sleep(1)
            item = random.randint(1, 100)
            print(f"生产了{item}")
            self.q.put(item)

#
# if __name__ == '__main__':
#     q = Queue()
#     c = Customer(q)
#     p = Productor(q)




# 协程写法 （yield）

