# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/28 7:06 PM

"""

from subprocess import call
from config import settings

class AllureHandle(object):

    def execute_command(self):
        try:
            call(settings.ALLURE_COMMAND, shell=True)
            call(settings.ALLURE_START_COMMAND, shell=True)


        except Exception as e:
            print("执行allure命令失败，详情参考：{}".format(e))