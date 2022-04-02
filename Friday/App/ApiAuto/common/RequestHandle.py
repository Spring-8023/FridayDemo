# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/17 6:13 PM

"""
import requests
from common import ExcelHandle
from config import settings
session = requests.session()

class RequestHandle():
    def __init__(self):
        self.session = session
        self.host = 'http://192.168.0.8'

    def send(self, url, method, **kwargs):

        url = self.host + url
        resp = self.session.request(url=url, method=method, **kwargs)
        return resp

    def send_msg(self, item):

        url = item['接口地址']
        method = item['接口请求方式']
        data = eval(item['请求参数'])
        resp = self.session.request(url=self.host+url, method=method, data=data)
        return resp


    def check_response(self, response, item):

        assert(response.status_code == item['期望响应状态码'])
        assert(response.json()['status'] == item['期望业务码'])

        if (item['测试编号'] == 'Login001' or item['测试编号'] == 'Login002'):
            assert response.json()['data']['student']['studentId'] == eval(item['响应预期结果'])['data']['student']['studentId']
        else:
            assert response.json()['data']['errorStr'] == eval(item['响应预期结果'])['data']['errorStr']


if __name__ == "__main__":
    pass