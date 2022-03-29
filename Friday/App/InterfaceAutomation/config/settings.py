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

# 数据文件路径,切换文件时，只需要更改文件名即可
EXCEL_FILE_PATH = os.path.join(DATA_PATH, 'Friday_data.xlsx')


# ---------------Allure相关-----------------
# 报告路径
REPORT_PATH = os.path.join(BASE_PATH, 'report')
# Allure的json文件夹命名：
ALLURE_JSON_DIR_NAME = 'allure_json'
# Allure的json文件路径：
ALLURE_JSON_DIR_PATH = os.path.join(REPORT_PATH, ALLURE_JSON_DIR_NAME)
# Allure的html文件夹命名：
# ALLURE_REPORT_DIR_NAME = os.path.join(REPORT_PATH, 'allure_report')
ALLURE_REPORT_DIR_NAME = 'allure_report'
# Allure的html报告路径：
ALLURE_REPORT_DIR_PATH = os.path.join(REPORT_PATH, ALLURE_REPORT_DIR_NAME)
# 压缩包路径：
ZIP_FILE_PATH = os.path.join(REPORT_PATH, 'report.zip')
# 生成报告命令：
ALLURE_COMMAND = "allure generate {} -o {} --clean".format(ALLURE_JSON_DIR_PATH, ALLURE_REPORT_DIR_PATH)
# 本地启动服务命令
ALLURE_START_COMMAND = 'allure open -h 127.0.0.1 -p 8880 {}'.format(ALLURE_REPORT_DIR_PATH)


# -------------------日志相关----------------
# 日志级别
LOG_LEVEL = 'debug'
LOG_STREAM_LEVEL = 'debug'   # 屏幕输出流
LOG_FILE_LEVEL = 'info'     # 文件输出流
# 日志文件夹命名
LOG_FILE_NAME = os.path.join(BASE_PATH, 'logs', datetime.datetime.now().strftime('%Y-%m-%d') + '.log')



