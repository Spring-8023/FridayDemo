# -*- coding:utf-8 -*-
import os
import yaml

cur_path = os.path.dirname(__file__)
# print
# 遍历当前文件路径下的所有yaml文件
def file_name():
    L = []
    k = {}
    for root, dirs, files in os.walk(cur_path):
        # print root
        # print dirs
        # print files
        for file in files:
            # print os.path.splitext(file)
            # print file
            if os.path.splitext(file)[1] == '.yaml':

                k[file] = root
                # print
                L.append(os.path.join(root, file))

    # print k
    # print L
    # for l in k:
    #     print l, k[l]
    #     print os.path.splitext(l)
    # print k
    return k  # 返回一个路径键值对

# 遍历当前文件路径下的所有yaml文件，并对读取yaml文件，return结果
def file_name2(param):
    L = []
    k = {}
    for root, dirs, files in os.walk(cur_path):
        # print root
        # print dirs
        # print files
        for file in files:
            # print os.path.splitext(file)
            # print file
            if os.path.splitext(file)[1] == '.yaml':

                k[file] = root
                # print
                L.append(os.path.join(root, file))

    for f in k:
        # print f
        if os.path.splitext(f)[0] == param:
            path = os.path.join(k[f], f)
            # print monitor_path
    config = open(path, 'r')
    d = yaml.load(config, Loader=yaml.FullLoader)
    return path, d  # 返回一个路径键值对

def get_Info():
    file = file_name()
    # print file

    for f in file:
        # print f
        if os.path.splitext(f)[0] == 'config':
            config_path = os.path.join(file[f], f)
            # print monitor_path

    config = open(config_path, 'r')
    d = yaml.load(config, Loader=yaml.FullLoader)
    config_info = d['Config']
    login_info = d['LoginInfo']
    # print ios_BasicInfo
    # print login_info
    return config_info, login_info

if __name__ == '__main__':
    # file_name()
    get_Info()
