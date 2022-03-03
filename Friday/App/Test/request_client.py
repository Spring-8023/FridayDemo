# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/3 5:24 PM

"""

import requests

session = requests.session()

def send(url,method,**kwargs):
    resp = session.request(url=url,method=method,**kwargs)
    return resp