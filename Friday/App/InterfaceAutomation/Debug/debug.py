# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/21 6:31 PM

"""
from common.RequestHandler import RequestHandle
from config import settings

from common.ExcelHandler import ExcelHandle


def send_debug():
    host = "http://192.168.0.8"

    a = ExcelHandle().read_excel(settings.EXCEL_FILE_PATH, "Sheet3")
    for resp in a:
        casename = resp[0]
        url = resp[1]
        method = resp[2]
        headers = resp[3]
        params = eval(resp[4])
        # print(casename)
        # print(url)
        # print(method)
        # print(headers)
        print(params)
        print(type(params))
        result = RequestHandle().send(url=host + url, method=method, headers=headers, **params)
        print(result.text)
    # for i in range(0, len(a)):
    # o = a[i]
    # print(o)
    # url = a[i].get('接口地址')
    # method = a[i].get('接口请求方式')
    # print(url)
    # print(method)

    a = ExcelHandle().get_excel_data(settings.EXCEL_FILE_PATH, "Sheet2")
    print(a)

    result = RequestHandle().send_(a)
    print(result)


# s= 2/1+3/2+...+22/21

def sum():
    s = 0
    for x in range(2, 22):
        y = x-1
        a = x/y
    s = s + a
    print(s)
if __name__ == "__main__":
    # send_debug()
    sum()