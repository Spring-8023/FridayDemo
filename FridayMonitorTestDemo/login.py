# -*— coding:utf-8 -*-
import requests
import test_read_data

def login():

    (config, logininfo) = test_read_data.get_Info()
    # print (logininfo)
    # 内网host使用参数 Intranet_host 外网host使用参数 Outside_host
    # 获取host
    host = config.get('Intranet_host')
    url = host + logininfo.get('url')
    print(url)
    data = logininfo.get('data')
    method = logininfo.get('method')
    s = requests.session()
    if method == 'POST':
        r = s.post(url=url, data=data)
        res = r.json()
        if res.get('data')['statusInt'] == 1:
            print("登陆成功")
            print(res)
            # print(res.get('data')['student'])
            return(s,r)
        else:
            errorTip = res.get('data')['errorStr']
            print("登陆失败,失败原因:" + errorTip)
            print(type(errorTip))
    else:
        print("登陆接口请求方式是post")

def get_studentinfo(r):
    pass

if __name__ == '__main__':
    login()