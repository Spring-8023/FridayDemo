# -*— coding:utf-8 -*-
import requests

class UpdateSystemUrl:
    def __init__(self):
        requests.post()
    def test_increase(self):
        data = {
            'url': 'http://jw.cuc.edu.cn/academic/common/security/login.jsp',
            'urlName': '教务系统',
            'remark': '',
            'level': 0,
            'status': '1',
            'schoolId': '1007',
        }

        # http://e.cuc.edu.cn/login?service=http://e.cuc.edu.cn/new/index.html 统一身份认证系统
        host = 'http://192.168.0.36:8086'
        url = host + '/Base/School/saveOrupdateSystemUrl.action'


        requests.post(url=url, params= data)
        print(requests.codes)

