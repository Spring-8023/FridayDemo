# -*- coding:utf-8 -*-

import requests

class TreeholeTestDemo():
    def __init__(self):
        print('开始构建DBUtil')

    def login(self):
        login_url = 'http://192.168.0.8:80/V2/StudentSkip/loginCheckV4.action'
        data = {
            'password': '54d87d745c5c90aeeff78b08b26d2ee6',
            # 'account': '4ab073e23f051f50fbc7107cb550400f',
        #    password    54d87d745c5c90aeeff78b08b26d2ee6
            'account': '7e657c97967e7f66255a9c93d84c63bd',
            # 'registrationId': '',
            'ifa': 'FA743629-436F-4EFA-B493-2A883B1D83CF',
            'ifv': '349305A8-D830-4D7C-B125-B2847BB2AC50',
            'versionNumber': '9.5.5',
            'platform': '2',
            'channel': 'AppStore',
            'phoneVersion': '12.2',
            'phoneModel': 'iPhone X',
            'phoneBrand': 'Apple'
          }
        header = ''
        res = requests.post(url=login_url, data=data)
        print(res.json())

    def

