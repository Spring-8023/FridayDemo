# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/9 3:56 PM

"""

# 该文件是pytest测试框架,使用pytest_collection_modifyitems钩子函数去除乱码
def pytest_collection_modifyitems(items):
    for item in items:
        #修改编码
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode_escape')
