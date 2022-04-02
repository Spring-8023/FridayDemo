# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/22 9:52 AM

"""
import pytest
import allure
import shutil
from common.ExcelHandle import ExcelHandle
from common.RequestHandle import RequestHandle
from common.AllureHandle import AllureHandle
from common.LoggerHandle import logger
from common.SendEmailHandle import SendEmailHandle
from config import settings


class TestCase1(object):

    # @classmethod
    # def setup_class(self):
    #     print("删除json文件")
    #     shutil.rmtree(settings.ALLURE_JSON_DIR_PATH)  # 报告生成后删除不需要的json文件,防止多次执行后产生越来越多的json文件


    @pytest.mark.parametrize('item', ExcelHandle().get_excel_data(settings.EXCEL_FILE_PATH, 'Sheet2'))
    def test_case(self, item):
        resp = RequestHandle().send_msg(item)
        # print(resp.text)
        # logger().info(item)
        allure.dynamic.feature(item['用例名称'])
        allure.dynamic.title(item['用例名称'])
        # print(resp.json()['status'])
        allure.dynamic.description(
            "<b style='color:red;'> 请求的url:</b>{}<br />"
            "<b style='color:red;'> 预期值:</b>{}<br/ >"
            "<b style='color:red;'>实际执行结果:</b>{}<br />".format(
                item['接口地址'],
                item['期望响应状态码'],
                resp.status_code
            )
        )
        RequestHandle().check_response(resp, item)



    test_data = ExcelHandle().read_excel(settings.EXCEL_FILE_PATH, 'Sheet1')
    @pytest.mark.parametrize('casename,url,method,headers,params,code,business_code,msg', test_data )
    def est_case1(self, casename, url, method, headers, params, code, business_code, msg):
        params = eval(params)
        print(params)
        resp = RequestHandle().send(url=url, method=method, **params)
        print(resp.content)

    @classmethod
    def tearDownClass(cls):

    # def teardown_class(self):
        logger().info('teardown_class')
        # 执行allure命令，生成allure报告
        print("执行allure命令,并启动服务")
        AllureHandle().execute_command()
        # 将测试报告打包并发送邮件
        SendEmailHandle().send_mail_msg()

