# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/17 6:13 PM

"""
# import pytest
import requests
# from common.ExcelHandler import ExcelHandler
# from config import settings
session = requests.session()

class RequestHandler():
    def __init__(self):
        self.session = session
        self.host = 'http://192.168.0.8'

    def send(self, url, method, **kwargs):

        url = self.host + url
        resp = self.session.request(url=url, method=method, **kwargs)
        return resp

    def send_msg(self, item):
        # host = "http://192.168.0.8"


        url = item['接口地址']
        method = item['接口请求方式']
        data = eval(item['请求参数'])
        # print(type(data.yaml))
        # print(data.yaml)
        resp = self.session.request(url=self.host+url, method=method, data=data)
        return resp
        '''
        for i in range(0, len(item)):
            url = host + item[i].get('接口地址')
            method = item[i].get('接口请求方式')
            data.yaml = eval(item[i].get('请求参数'))

            resp = self.session.request(url=url, method=method, data.yaml=data.yaml)
            resp.status_code
            # print(resp.text)
            return resp
        '''
    def check_response(self, response, item):
    #
        assert(response.status_code == item['期望响应状态码'])
        assert(response.json()['status'] == item['期望业务码'])


if __name__ == "__main__":
    pass