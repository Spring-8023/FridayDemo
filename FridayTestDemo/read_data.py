# -*- coding:utf-8 -*-

import xlrd
import json
import numpy as np

def read_file():
    filepath = '/Users/mac-mini/Desktop/ApiData.xlsx'
    workbook = xlrd.open_workbook(filename=filepath)
    sheet_name = workbook.sheet_names()[1]
    print(sheet_name)
    sheet = workbook.sheet_by_name(sheet_name)
    print(sheet.cell_value(1,0))
    start = 1
    end = 5
    list_values = []
    for x in range(start, end):
        values = []
        row = sheet.row_values(x)
        for i in range(0, 3):
            values.append(row[i])
            # print(values)
        list_values.append(values)
        print(list_values)
    datamatrix = np.array(list_values)
    print()





if __name__ == '__main__':
    read_file()