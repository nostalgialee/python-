# -*- coding:utf-8 -*-
# @Time    : 2022/6/22 17:44
# @File    : inheritance.py
# Author: lee


# 抽象类 --- 单继承的规范
from abc import ABCMeta, abstractmethod

class InterfaceA(metaclass=ABCMeta):

    @abstractmethod
    def func(self):
        # 抽象类不可实例化，只能作为具体的类的规范
        # 子类必须要重写该方法

        pass

        """
        接口类的由来：--- 多继承的规范
            java 中没有多继承，所以发明了接口来多继承
            python 中没有接口类的语法，
            只能通过多继承模仿接口类的效果
        
        区别：
            # 抽象类中可以完成简单的代码，
            # 接口类中不能写具体的实现方法            
        """





# 封装
class A:

    def __init__(self):
        self.a = ''

    @property # 将方法伪装成属性
    def func(self):
        return

    @classmethod # 将对象方法转化为类方法
    def func1(cls):
        # cls 表示 类
        """
        1.有时候我们需要修改类的静态变量和类变量
        2.self 此时没有任何关联
        3.我们希望接受的是是 cls(类) 而不是self(对象)
        :return:
        """
        return

    @staticmethod
    # 定义为静态方法，无参数
    # 可以使用类调用，也可以使用对象调用
    def func2():
        pass