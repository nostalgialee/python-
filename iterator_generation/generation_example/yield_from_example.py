# -*- coding:utf-8 -*-
# @Time    : 2022/6/21 13:51
# @File    : yield_from_example.py
# Author: lee

from collections import namedtuple

Result = namedtuple('Result', ['count', 'average'])


def averager():
    total = 0.0
    count = 0
    average = 0
    while True:
        temp = yield
        if temp is None:
            break
        total += temp
        count += 1
        average = total / count
    return Result(count, average)


def grouper(results, key):
    while True:
        results[key] = yield from averager()
        # {'girls': }

def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


def main(data):
    results = {}
    group = None
    for k, v in data.items():
        group = grouper(results, k)
        next(group)
        for v_ in v:
            group.send(v_)
        group.send(None)
    report(results)
    if group:  # 停止委派器生成器
         group.close()


data = {
    'girls;kg': [40, 41, 42, 43, 44, 54],
    'girls;m': [1.5, 1.6, 1.8, 1.5, 1.45, 1.6],
    'boys;kg': [50, 51, 62, 53, 54, 54],
    'boys;m': [1.6, 1.8, 1.8, 1.7, 1.55, 1.6],
}

if __name__ == '__main__':
    main(data)
