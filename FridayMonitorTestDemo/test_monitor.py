# -*- coding:utf-8 -*-
import requests
from ddt import ddt, file_data, unpack
from FridayMonitorTestDemo import test_read_data, send_error, login
# import test_read_data
import os
import unittest
# import send_error
import json
import logging

monitor_path, d = test_read_data.file_name2('api_data')

@ddt
class MonitortDemo(unittest.TestCase):

    @classmethod
    def setUpClass(scl):
        MonitortDemo.logger = logging.getLogger()
        MonitortDemo.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # 使用FileHandelr输出到文件
        fh = logging.FileHandler('log.txt')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        # 使用StreamHandler输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        MonitortDemo.logger.addHandler(fh)
        MonitortDemo.logger.addHandler(ch)

        # 获取文件名为"config"的yaml文件，并读取yaml文件返回
        monitor_path, d = test_read_data.file_name2('config')
        # 获取config.yaml文件中的Config部分信息
        config = d['Config']
        # 获取config.yaml文件中的LoginInfo部分信息
        logininfo = d['LoginInfo']
        # 内网host使用参数 Intranet_host 外网host使用参数 Outside_host
        # 获取host
        MonitortDemo.host = config.get('Intranet_host')
        # 获取基础信息
        MonitortDemo.BasicInfo = config.get('BasicInfo')
        # 登录软件并返回登录的ssession已经登录后的结果
        MonitortDemo.res, MonitortDemo.result = login.login(MonitortDemo.host, logininfo)



    @file_data(monitor_path)
    def test_monitor(self, **data):
        # 获取登录的学生id
        studentID = login.get_studentinfo(MonitortDemo.result).get('studentId')
        # print(studentID)
        url = MonitortDemo.host + data['url']
        method = data['method']
        params = data['data']
        # print(type(params))
        params.update(MonitortDemo.BasicInfo)
        # 判断参数中是否存在学生id，如果存在把key值改为获取到的学生id
        if ('studentId' in params.keys()):
            params['studentId'] = studentID
        # print(params)
        print(url)
        if method == 'POST':
            try:
                res = MonitortDemo.res.post(url=url, data=params, timeout=60)
                httpCode = res.status_code
                httpResult = res.text
                # print(type(httpCode), type(httpResult))
                print(res.json())
                if httpCode != 200:
                    send_error.sendEmail("监控报警: \n报警接口: " + url + " \n接口返回状态码：%s " % str(httpCode) + "\n接口返回结果：" + httpResult)
                elif json.loads(httpResult).get('status') == -1:
                    send_error.sendEmail("监控报警: \n报警接口: " + url + " \n接口返回状态码：%s " % str(httpCode) + "\n接口返回结果：" + httpResult)
                else:
                    # print("成功访问")
                    MonitortDemo.logger.info('成功访问')

            except requests.exceptions.Timeout as e:
                print(type(e))
                httpResult = str(e)
                send_error.sendEmail("监控报警:" + url + "\n访问超时：" + httpResult)

        elif method == 'GET':
            try:
                res = MonitortDemo.res.get(url=url, data=params, timeout=60)
                # print res.status_code
                httpCode = res.status_code
                httpResult = res.text
                # print type(res)
                if httpCode != 200:
                    send_error.sendEmail("监控报警: \n报警接口: " + url + " \n接口返回状态码：%s " % str(httpCode) + "\n接口返回结果：" + httpResult)
                else:
                    print("成功访问")
                    # MonitortDemo.logger.info('get成功访问')

            except requests.exceptions.Timeout as e:
                httpResult = str(e)
                send_error.sendEmail("监控报警:" + url + "\n访问超时：" + httpResult)



if __name__ == '__main__':

    unittest.main()
    # m.read_yaml()