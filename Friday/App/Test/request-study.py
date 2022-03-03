# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/2 3:49 PM

"""

import requests

session = requests.session()
host = "http://192.168.0.8"
url = "/V2/StudentSkip/loginCheckV4.action"
data = {
    "account": "lcj1@xt.com",
    "password": "134679",
    "updateInfo": "false",
    "deviceCode": "",
    "versionNumber": "9.8.3",
    "platform":	1,

}
print(data)
fixed_data = {
    "phoneModel": "V1829A",
    "phoneBrand": "vivo",
    "channel": "SoftwareUpdate",
    "platform":	1,
    "phoneVersion": 29,
    "versionNumber": "9.8.4",
    "source": "Friday_android"
}
data.update(fixed_data)
print(data)

resp = session.request(url=host+url, data=data, method="post")

print(resp.text)
