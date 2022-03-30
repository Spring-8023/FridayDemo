# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/17 4:21 PM

"""

import os
import sys
import datetime

#根目录
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# -----------Excel相关---------
# 数据文件夹路径
DATA_PATH = os.path.join(BASE_PATH, 'params')

EXECL_FILE_NAME = 'Friday_data.xlsx'
# 数据文件路径,切换文件时，只需要更改文件名即可
EXCEL_FILE_PATH = os.path.join(DATA_PATH, EXECL_FILE_NAME)


# ---------------Allure相关配置-----------------
# 报告路径
REPORT_PATH = os.path.join(BASE_PATH, 'report')
# Allure的json文件夹命名：
ALLURE_JSON_NAME = 'allure_json'
# Allure的json文件路径：
ALLURE_JSON_PATH = os.path.join(REPORT_PATH, ALLURE_JSON_NAME)
# Allure的html文件夹命名：
# ALLURE_REPORT_DIR_NAME = os.path.join(REPORT_PATH, 'allure_report')
ALLURE_REPORT_NAME = 'allure_report'
# Allure的html报告路径：
ALLURE_REPORT_PATH = os.path.join(REPORT_PATH, ALLURE_REPORT_NAME)
# 压缩包路径：
ZIP_FILE_PATH = os.path.join(REPORT_PATH, 'report.zip')
# 生成报告命令：
ALLURE_COMMAND = "allure generate {} -o {} --clean".format(ALLURE_JSON_PATH, ALLURE_REPORT_PATH)
# 本地启动服务命令
ALLURE_START_COMMAND = 'allure open -h 127.0.0.1 -p 8880 {}'.format(ALLURE_REPORT_PATH)


# -------------------日志相关配置----------------
# 日志级别
LOG_LEVEL = 'debug'
LOG_STREAM_LEVEL = 'debug'   # 屏幕输出流
LOG_FILE_LEVEL = 'info'     # 文件输出流
# 日志文件夹命名
LOG_FILE_NAME = os.path.join(BASE_PATH, 'logs', datetime.datetime.now().strftime('%Y-%m-%d') + '.log')

# ----------------------邮件相关配置------------
MAIL_HOST = 'smtp.exmail.qq.com'  # 腾讯企业邮箱
MAIL_USER = 'fiona@myfriday.cn'
MAIL_PWD = 'oGyuD4Jh9o2Pgs6W'

# 邮件发件人
SENDER = 'fiona@myfriday.cn'
# 邮件收件人,邮件收件人可以有多个，以列表形式存放
RECEIVERS = ['1517437552@qq.com', 'fiona@myfriday.cn']

# 邮件主题、收件人、发件人
MAIL_SUBJECT = '接口自动化测试报告'
MAIL_FROM = '接口自动化测试中心'
MAIL_TO = '项目相关人员'

# 邮件正文
MAIl_CONTENT = 'hi all: \r\n    这是接口自动化测试报告,详情请下载附件\n    查看方法：终端执行 allure open report \n\n\n测试人:{execute_tester_name}\n联系方式:{execute_tester_phone} \n测试执行时间：{execute_tests_data}'.format(
    execute_tester_name="Spring",
    execute_tester_phone=15889950579,
    execute_tests_data=datetime.datetime.date(datetime.datetime.now())
)

