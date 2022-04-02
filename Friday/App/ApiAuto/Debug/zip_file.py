# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/29 6:50 PM

"""

import shutil
import zipfile
import os
import datetime
from config import settings

# shutil.make_archive('/Volumes/HDD/Code/Python/FridayDemo/Friday/App/ApiAuto/Debug/', "zip", root_dir='/Users/mac-mini/Desktop/约面0330')
zip_dir = '/Volumes/HDD/Code/Python/FridayDemo/Friday/App/ApiAuto/Debug/'
new_file_path = os.path.join(zip_dir, 'test1.zip')
zip_file_path = '/Volumes/HDD/Code/Python/FridayDemo/Friday/App/ApiAuto/Debug/'

create_zip_file = zipfile.ZipFile(new_file_path, mode='w', compression=zipfile.ZIP_DEFLATED)


# create_zip_file.write(os.path.join(zip_file_path, 'SendEmailTest.py'), 'SendEmailTest.py')

# datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
for dir_path, dir_name, file_names in os.walk(settings.ALLURE_REPORT_DIR_PATH):
    file_path = dir_path.replace(settings.ALLURE_REPORT_DIR_PATH, '')
    file_path = file_path and file_path + os.sep or ''
    # print(file_path)
    # print(dir_name)
    for file_name in file_names:
        create_zip_file.write(os.path.join(dir_path, file_name), (file_path + file_name))
        # print(os.path.join(dir_path, file_name))
        #
        # print("-------------")
        # print(file_path + file_name)
        # print("-----分割线-----")
