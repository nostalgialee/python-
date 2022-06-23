# -*- coding:utf-8 -*-
# @Time    : 2022/6/22 21:33
# @File    : _metaclass.py
# Author: lee

# 元类 --- 它的作用是定制类的创建行为


# 一、class also object

class Foo:





    def func(self):
        print("This is func")
        return




# 类创建对象
#     1. 执行 __new__ 方法，创建对象（空对象）
    # def __new__(cls, *args, **kwargs):
    #     # 构造方法
    #     data = object.__new__(cls)
    #     return data

#     2. 执行 __init__ 方法，初始化对象 (初始化方法)


# foo = Foo()
# print(type(foo))
# <class '__main__.Foo'>

# print(type(foo.func))
# <class 'method'>

# print(type(Foo))
# Foo 类也是一个对象
# <class 'type'> 属于 Type 类










# 二、谁创建的类？ 动态创建 class（类）
# 类默认由 type 创建

# 传统方式
class Foo1(object):
    v1 = 1
    def func(self):
        return 2

# 非传统方式
Foo2 = type('Foo2', (object, ),
            {'v1': 1, 'func':lambda self:2})

    # 参数说明：
        # 类名
        # 父类
        # 成员








# 三、类默认由 type 创建，怎么让创建类的 thing 改成其他东西呢？
# 元类 --- 创建（类对象）
    # 类也是一个对象，是对象，必然有 thing 去创建，
    # 创建 类的 thing 就称为 元类

# metaclass的主要目的是在class被创建的时候对生成的class进行自动的动态修改。

class MyType(type):
    """
    既然 类 是有type创建的，所以我们构造新的元类的时候
    就是继承 type, 并重写
    """

    def __new__(cls, *args, **kwargs):
        # TODO:
        # 创建类的时候进行拓展

        # print("new")
        new_cls = super().__new__(cls, *args, **kwargs)
        # or
        # new_cls = type.__new__(cls, *args, **kwargs)

        return new_cls

    def __init__(self, *args, **kwargs):
        # TODO:
        # 创建类的时候进行拓展

        # print("init")
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        # 实例化对象 + () 进行调用
        # 这里就是 new_cls() 即为 类(Foo3)实例化

        # 1.调用 __new__ 子类(new_cls)创建子类对象
        # 2.调用 __init__, 初始化子类


        # TODO:
        # 创建类(new_cls)的初始化对象 的时候进行拓展


        cls_obj = self.__new__(self)
        self.__init__(cls_obj, *args, **kwargs)
        return cls_obj



class Foo3(metaclass=MyType):

    """
    Foo3 就是 MyType 创建的一个对象
    Foo3 = MyType()

    """

    def __init__(self, name):
        self.name = name


f = Foo3('alex') # 调用的元类的__call__方法
# print(f.name)











# 四、应用 --- 单例模式 （元类构造单例模式）

class SingleType(type):


    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        return obj

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance:
            return self._instance
        self._instance = self.__new__(self)
        self.__init__(self._instance, *args, **kwargs)
        return self._instance



class Foo4(metaclass=SingleType):

    a = 1
    b = 3
    c = 4

    def __init__(self, name):
        self.name = name


a1 = Foo4('a')
b2 = Foo4('b')

# print(a1)
# print(b2)












####分析一下 django orm model 的源码


def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.
    class metaclass(meta):

        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)
            # class name(bases, metaclass=meta) 创建类对象

            # return type(name, bases, d)
            # 上面的语句：
                # class name(bases, metaclass=type)
    return type.__new__(metaclass, 'temporary_class', (), {})
    # 如下是上面的这一句的来源
    # 因为 metaclass(meta):
        # 而 meta 是 继承 type 的

    # metaclass 调用父亲 type 的 __new__ 即返回了 meta 元类
    # return meta('temporary_class', (), {})
    # 创建了 temporary_class 类对象，
    # 而且 Model(temporary_class) 继承了 temporary_class

    # 综上所述：
    #     自定义的元类 创建了 temporary_class 类对象，然后 Model 继承了 temporary_class






#


# class Model(six.with_metaclass(ModelBase)):
#     # ModeBase 继承了 type 所以 ModelBase 可以创建类
#
#     def __init__(self, *args, **kwargs):
#         # Alias some things as locals to avoid repeat global lookups
#         cls = self.__class__
#         opts = self._meta
#         _setattr = setattr
#         _DEFERRED = DEFERRED
#
#         pre_init.send(sender=cls, args=args, kwargs=kwargs)
#
#         # Set up the storage for instance state
#         self._state = ModelState()



# 具体分析
# https://learnku.com/articles/32675

from django.db import models

class ModelBase(type):
    # 元类 --- ModelBase 继承了 type，实现了 5 个方法

    def __new__(cls, name, bases, attrs, **kwargs):
        # 而且能够实现字段生成属性的功能也来源于此。
        ...

    def add_to_class(cls, name, value):
        ...

    def _prepare(cls):
        ...

    def _base_manager(cls):
        ...

    def _default_manager(cls):
        ...



class UserModel(models.Model):
    pass



class Model(with_metaclass(ModelBase)):
    pass