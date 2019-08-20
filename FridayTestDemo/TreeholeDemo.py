# -*- coding:utf-8 -*-

import requests

class TreeholeTestDemo():
    def __init__(self):
        print('开始构建DBUtil')
        self.s = requests.session()
        self.header = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 -SuperFriday_9.5.5 lite_1.0.0', 'Content_type': 'application/x-www-form-urlencoded; charset=utf-8'}

    def login(self):
        login_url = 'http://192.168.0.8:80/V2/StudentSkip/loginCheckV4.action'
        data = {
            'password': '54d87d745c5c90aeeff78b08b26d2ee633',
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
        try:
            res = self.s.post(url=login_url, data=data, headers=self.header, timeout=60)
            if res.json()['data'].get('statusInt') == 1:
                print('登录成功')
                print(res.json())
                # print(res.headers)
            elif res.json()['data'].get('statusInt') == 0:
                print('登录失败，失败原因：' + res.json()['data'])

        except Exception as e:
            print('出现异常情况：' + str(e))




    def issueMessage(self):
        url = 'http://192.168.0.8:80/V2/Treehole/Message/issueMessageV5.action'
        data = {
            'content': '测试一下',
            'source': 'Friday_iOS',
            'pageSource': 0,
            'isRelayedComment': 0,
            'anonymous': 0,
            'versionNumber': '9.5.5',
            'platform': 2,
            'channel': 'AppStore',
            'phoneVersion': 12.2,
            'phoneModel': 'iPhoneX',
            'phoneBrand': 'Apple'
        }

        # print(res.json())
        try:
            res = self.s.post(url=url, data=data, timeout=60)
            if res.json()['status'] == 1:
                print('发布成功')
            elif res.json()['status'] == -1:
                print('发送失败，失败原因：' + res.json()['message'])

        except Exception as e:
            print('出现异常情况：' + str(e))




