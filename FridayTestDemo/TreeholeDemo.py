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
        try:
            res = self.s.post(url=login_url, data=data, headers=self.header, timeout=60)
            status = res.json()['data'].get('statusInt')
            if status == 1:
                print('登录成功')
                print(res.json())
                # print(res.headers)
            elif status == 0:
                print('登录失败，失败原因：' + res.json()['data'].get('errorStr'))
            return res
        except Exception as e:
            print('出现异常情况：' + str(e))

    # 发布帖子
    def issueMessage(self,login_res):
        status = login_res.json()['data'].get('statusInt')

        url = 'http://192.168.0.8:80/V2/Treehole/Message/issueMessageV5.action'
        data = {
            'content': '文案测',
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
        if status == 1:
            try:
                res = self.s.post(url=url, data=data, timeout=60)
                if res.json()['status'] == 1:
                    print('发布成功')
                    print(res.json())
                elif res.json()['status'] == -1:
                    print('发送失败，失败原因：' + res.json()['message'])

            except Exception as e:
                print('出现异常情况：' + str(e))
        elif status == 0:
            print('发布失败，失败原因：登录失败！->登录失败原因：' + login_res.json()['data'].get('errorStr'))
        # print(res.json())

    # 评论帖子
    def Comment(self, login_res):
        status = login_res.json()['data'].get('statusInt')
        comment_url = 'http://192.168.0.8:80/Treehole/V4/Comment/comment.action'
        data = {
            'messageId': 57462110,
            'content': 'Etta',
            'source': 'Friday_iOS',
            'plateId': 1,
            'anonymous': 'false',
            'versionNumber': '9.5.5',
            'platform': 2,
            'channel': 'AppStore',
            'phoneVersion': 12.2,
            'phoneModel': 'iPhoneX',
            'phoneBrand': 'Apple'
        }
        if status == 1:
            try:
                res = self.s.post(url=comment_url, data=data, timeout=60)
                if res.json()['status'] == 1:
                    print('评论成功')
                    print(res.json())
                elif res.json()['status'] == -1:
                    print('评论发送失败，失败原因：' + res.json()['message'])

            except Exception as e:
                print('出现异常情况：' + str(e))
        elif status == 0:
            print('评论发送失败，失败原因：登录失败！->登录失败原因：' + login_res.json()['data'].get('errorStr'))
        # print(res.json())

        def Delete_Comment(self, login_res):
            status = login_res.json()['data'].get('statusInt')
            delete_comment_url = 'http://192.168.0.8:80/Treehole/V4/Comment/delete.action'
            data = {
                'commentId': 57462110,
                'plateId': 1,
                'versionNumber': '9.5.5',
                'platform': 2,
                'channel': 'AppStore',
                'phoneVersion': 12.2,
                'phoneModel': 'iPhoneX',
                'phoneBrand': 'Apple'
            }
            if status == 1:
                try:
                    res = self.s.post(url=delete_comment_url, data=data, timeout=60)
                    if res.json()['status'] == 1:
                        print('删除成功')
                        print(res.json())
                    elif res.json()['status'] == -1:
                        print('评论删除失败，失败原因：' + res.json()['message'])

                except Exception as e:
                    print('出现异常情况：' + str(e))
            elif status == 0:
                print('评论删除失败，失败原因：登录失败！->登录失败原因：' + login_res.json()['data'].get('errorStr'))
            # print(res.json())

    # 点赞
    def Like(self, login_res):
        status = login_res.json()['data'].get('statusInt')
        like_url = 'http://192.168.0.8:80/Treehole/V4/Like/like.action'
        data = {
            'messageId': 57462110,
            'plateId': 1,
            'versionNumber': '9.5.5',
            'platform': 2,
            'channel': 'AppStore',
            'phoneVersion': 12.2,
            'phoneModel': 'iPhoneX',
            'phoneBrand': 'Apple'
        }
        if status == 1:
            try:
                res = self.s.post(url=like_url, data=data, timeout=60)
                if res.json()['status'] == 1:
                    print('点赞成功')
                    print(res.json())
                elif res.json()['status'] == -1:
                    print('点赞失败，失败原因：' + res.json()['message'])

            except Exception as e:
                print('出现异常情况：' + str(e))
        elif status == 0:
            print('点赞失败，失败原因：登录失败！->登录失败原因：' + login_res.json()['data'].get('errorStr'))
        # print(res.json())

