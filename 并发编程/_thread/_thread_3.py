# -*- coding:utf-8 -*-
# @Time    : 2022/6/26 21:40
# @File    : _thread_3.py
# Author: lee


# 0.案例

from threading import Thread

count = 0


def add_func():
    global  count
    for i in range(20000):
        count += 1


def sub_func():
    global  count
    for i in range(20000):
        count -= 1

t_l = []
for i in range(5):
    t1 = Thread(target=add_func)
    t1.start()
    t_l.append(t1)
    t2 = Thread(target=sub_func)
    t2.start()
    t_l.append(t2)

for t in t_l:
    t.join()

# print(count) # >>> 0
# 但是存在一种可能行：
#         线程1 count += 1，但是未来得及赋值给全局变量，
#         便切换至线程2，此时便会产生了数据安全
#         解决方案：加锁



# 一、互斥锁 --- 保证一个线程未执行完毕之前，不会有另外的线程执行
# 注意与 GIL 锁的区别
"""
    应用场景：
        1.对于全局变量的修改
        2.对于某个值的 + - * /
    
    """





# 二、递归锁
from threading import Thread, Lock, RLock

"""
Rlock实例化之后该对象可以在⼀个线程⼀直acquire，
没有release，其他对象不能获取锁；

Lock是互斥锁，同⼀时间只能在⼀个线程/进程acquire()⼀次,
没有release，其他对象不能获取锁。

"""

# 对比 互斥锁与递归锁
l = Lock()
rl = RLock()

def eat_lock(name):
    l.acquire()
    print('%s eat' % name)
    l.acquire()
    print('%s finished' % name)
    l.release()
    print('')
    l.release()


def eat_rlock(name):
    rl.acquire()
    print('%s eat' % name)
    rl.acquire()
    print('%s finished' % name)
    rl.release()
    rl.release()


t11 = Thread(target=eat_lock, args=('Sam',))
t12 = Thread(target=eat_lock, args=('Sunny',))
t21 = Thread(target=eat_rlock, args=('Tom',))
t22 = Thread(target=eat_rlock, args=('Tonny',))


# t11.start()
# t12.start() # 发生死锁现象


t21.start()
t22.start() # 不会发生死锁现象









# 三、死锁
