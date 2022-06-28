# -*- coding:utf-8 -*-
# @Time    : 2022/6/27 13:26
# @File    : _thread_4.py
# Author: lee


# 线程池
# 写个例子吧 --- 具体知识点在 进程池 文件中

# 爬取各大网站的大小实例

import os
import requests
from concurrent.futures import ThreadPoolExecutor

URLS = [

        'https://zhuanlan.zhihu.com',
        'https://www.cnblogs.com',
        'https://www.python.org',
        'https://blog.csdn.net',
        'http://www.china.com.cn',

]


def get_html(url):
    print(f"线程:{os.getpid()}正在获取网站:{url}源码")
    response = requests.get(url)
    if response.status_code == 200:
        return {"url": url, "text": response.text}
    else:
        return {"url": url, "text": ""}


def parse_html(back):
    res = back.result()
    print(f"线程:{os.getpid()}正在解析网站:{url}源码")
    with open("html_size.txt", "a")as f:
        f.write(f"url:{res['url']},size:{len(res['text'])}\n")


with ThreadPoolExecutor(3) as tpool:

    for url in URLS:
        f = tpool.submit(get_html, url)
        f.add_done_callback(parse_html)
