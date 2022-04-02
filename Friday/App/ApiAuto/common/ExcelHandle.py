# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/17 10:03 AM

"""

import openpyxl
import xlrd
from config import settings

class ExcelHandle():

    def __init__(self, excel_file_path=None):
        self.excel_file_path = excel_file_path

    def get_excel_data(self, excel_file_path, sheet_name):
        book = xlrd.open_workbook(excel_file_path)
        sheet_data = book.sheet_by_name(sheet_name)
        # 获取标题：
        title = sheet_data.row_values(0)

        # 方式一循环添加返回列表：
        l = []
        for row in range(1, sheet_data.nrows):
        #     # print(sheet_data.row_values(row))
        #     #zip()函数，用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，返回由这些元组组成的列表
            l.append(dict(zip(title, sheet_data.row_values(row))))
        return l
        # 方式二列表解析式返回：
        # return [dict(zip(title, sheet_data.row_values(row))) for row in range(1, sheet_data.nrows)]



    def read_excel(self, excel_file_path, sheet_name):
        book = xlrd.open_workbook(excel_file_path)
        sheet_data = book.sheet_by_name(sheet_name)

        l = []
        for row in range(1, sheet_data.nrows):
            l.append(sheet_data.row_values(row))

        return l

    def read_excel_data(self, excel_file_path, sheet_name, runCase=['all']):
        book = xlrd.open_workbook(excel_file_path)
        sheet_data = book.sheet_by_name(sheet_name)
        # print(sheet_data.row_values(0))
        title = sheet_data.row_values(0)
        runList = []
        if 'all' in runCase:
            # print("all")
            for row in range(1, sheet_data.nrows):
                # print(row)
                # print(sheet_data.row_values(row))
                # zip()函数，用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，返回由这些元组组成的列表
                runList.append(dict(zip(title, sheet_data.row_values(row))))
                # print(runList)
        else:
            for num in runCase:
                if '-' in num:
                    # print("-")
                    start, end = num.split('-')
                    # print(start + "-" + end)
                    for i in range(int(start), int(end)+1):
                        # print(i)
                        runList.append(dict(zip(title, sheet_data.row_values(i))))
                        # print(runList)
                else:
                    # print("shuzi")
                    runList.append(dict(zip(title, sheet_data.row_values(int(num)))))

        return runList


if __name__ == "__main__":
    # result = ExcelHandle().get_excel_data((settings.EXCEL_FILE_PATH), '登录')
    # result = ExcelHandle().read_excel_data(settings.EXCEL_FILE_PATH, '登录', runCase=['4-10'])
    result = ExcelHandle().read_excel_data(settings.EXCEL_FILE_PATH, '登录')
    print(result)
    # print(eval(result[0]['响应预期结果'])['data'])
