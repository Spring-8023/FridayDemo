# -*- coding:utf-8 -*-
import requests
from ddt import ddt, file_data, unpack
import test_read_data
import os
import unittest
import send_error
import json
import logging

file = test_read_data.file_name()
for f in file:
    if os.path.splitext(f)[0] == 'monitor':
        monitor_path = os.path.join(file[f], f)
        print monitor_path

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




    @file_data(monitor_path)
    def test_monitor(self, **data):
        url = data['url']
        method = data['method']
        params = data['data']
        if method == 'POST':
            try:
                res = requests.post(url=url, data=params, timeout=60)
                # print res.status_code
                httpCode = res.status_code
                httpResult = res.content
                # print type(httpResult)
                if httpCode != 200:
                    send_error.sendEmail(
                        "监控报警: \n报警接口: " + url + " \n接口返回状态码：%s " % httpCode + "\n接口返回结果：" + httpResult)
                elif json.loads(httpResult).get('status') == -1:
                    send_error.sendEmail("监控报警: \n报警接口: " + url + " \n接口返回状态码：%s " % httpCode + "\n接口返回结果：" + httpResult)
                else:
                    pass
                    # print "成功访问"
                    MonitortDemo.logger.info('成功访问')

            except requests.exceptions.Timeout, e:
                print e
                httpResult = str(e)
                send_error.sendEmail("监控报警:" + url + "\n访问超时：" + httpResult)

        elif method == 'GET':
            try:
                res = requests.get(url=url, data=params, timeout=60)
                # print res.status_code
                httpCode = res.status_code
                httpResult = res.content
                # print type(res)
                if httpCode != 200:
                    send_error.sendEmail(
                        "监控报警: \n报警接口: " + url + " \n接口返回状态码：%s " % httpCode + "\n接口返回结果：" + httpResult)
                else:
                    pass
                    print "成功访问"
                    # MonitortDemo.logger.info('get成功访问')

            except requests.exceptions.Timeout, e:
                print e
                httpResult = str(e)
                send_error.sendEmail("监控报警:" + url + "\n访问超时：" + httpResult)



if __name__ == '__main__':

    unittest.main()
    # m.read_yaml()