# -*- coding:utf-8 -*-
import requests
import smtplib  # python3 直接导入smtplib模块
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

def sendErrorMsg(msg):
    msgAccount = 'j01585'
    msgPassword = '663521'
    msgUrl = "http://61.145.229.29:9003/MWGate/wmgw.asmx/MongateCsSpSendSmsNew"
    msgData = {
        'userId': msgAccount,
        'password': msgPassword,
        'pszMobis': '15889950579',
        'pszMsg': "超级课程表监控系统：" + msg,
        'iMobiCount': '1',  # 手机号的数量
        'pszSubPort': '1'
    }
    res = requests.post(url=msgUrl, data=msgData)
    print(res.content)

def sendEmail(message):

    mail_info = {
        "from": "fiona@myfriday.cn",
        # "to": "1517437552@qq.com",
        "to": "fiona@myfriday.cn",
        "hostname": "smtp.exmail.qq.com",
        "username": "fiona@myfriday.cn",
        "password": "aXAA0dcAbl5gvaB0",
        "mail_subject": "超级课程表监控系统",
        "mail_text": message,
        "mail_encoding": "utf-8"
    }

    # 这里使用SMTP_SSL就是默认使用465端口
    smtp = SMTP_SSL(mail_info["hostname"])
    # 显示调试信息
    # smtp.set_debuglevel(1)

    smtp.ehlo(mail_info["hostname"])
    smtp.login(mail_info["username"], mail_info["password"])

    msg = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
    msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]

    try:
        smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


    smtp.quit()

if __name__ == '__main__':
    # sendErrorMsg("测试")
    sendEmail("测试")
    # pass