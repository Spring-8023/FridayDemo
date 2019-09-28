# -*- coding:utf-8 -*-
from FridayTestDemo import TreeholeDemo

if __name__ == '__main__':
    a = TreeholeDemo.TreeholeTestDemo()
    login_res = a.login()
    # a.issueMessage(login_res)
    a.Comment(login_res)