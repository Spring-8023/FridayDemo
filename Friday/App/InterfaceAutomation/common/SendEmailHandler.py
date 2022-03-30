# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/29 4:48 PM

"""

import zipfile
import os
import smtplib
import shutil
from config import settings
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from common.LoggerHandler import logger

class SendEmailHandler(object):

    # 压缩report功能
    def _compress_zip_file(self):
        # 将报告中的文件压缩，报告文件路径
        base_dir = settings.ALLURE_REPORT_PATH
        # 压缩包的路径
        zip_file_path = settings.ZIP_FILE_PATH
        # 创建压缩包对象 mode:a 表示继续添加 w表示覆盖文件 r
        zip_file = zipfile.ZipFile(zip_file_path, mode="w", compression=zipfile.ZIP_DEFLATED)

        for dir_path, dir_name, file_names in os.walk(base_dir):
            # 不replace，就从根目录开始复制
            file_path = dir_path.replace(base_dir, '')
            file_path = file_path and file_path + os.sep or ''
            for file_name in file_names:
                zip_file.write(os.path.join(dir_path, file_name), (file_path + file_name))

        zip_file.close()

    # 发送测试报告邮件功能
    def _send_mail(self):
        # 第三方SMTP服务
        mail_host = settings.MAIL_HOST

        # 登录邮箱的账号密码
        mail_user = settings.MAIL_USER
        main_pwd = settings.MAIL_PWD

        # 邮件发送人、收件人
        sender = settings.SENDER
        receivers = settings.RECEIVERS

        # 创建一个带附件的实例对象
        message = MIMEMultipart()

        # 邮件主题、收件人、发件人
        subject = settings.MAIL_SUBJECT
        message['Subject'] = Header(subject, 'utf-8')
        message['From'] = Header("{}".format(sender), 'utf-8')
        # message['From'] = Header(settings.MAIL_FROM, 'utf-8')
        message['To'] = Header("{}".format(';'.join(receivers)), 'utf-8')
        # message['To'] = Header(settings.MAIL_TO, 'utf-8')

        # 邮件正文内容 Html形式邮件：相当于是一个报告预览：
        content = settings.MAIl_CONTENT

        html = MIMEText(_text=content, _subtype='plain', _charset='utf-8')

        send_file = open(settings.ZIP_FILE_PATH, 'rb').read()
        text_att = MIMEText(_text=send_file, _subtype='base64', _charset='utf-8')
        text_att['Content-type'] = 'application/octet-stream'
        file_name = 'report.zip'
        text_att.add_header('Content-Disposition', 'attachment', filename="{}".format(file_name))
        message.attach(html)
        message.attach(text_att)

        try:
            smtp_obj = smtplib.SMTP_SSL(mail_host)
            # SMTP_SSL对象后，需要调用ehlo()方法，向SMTP电子邮件服务器“打招呼”，这是SMTP的第一步，对于建立到服务器的连接很重要
            smtp_obj.ehlo(mail_host)
            smtp_obj.login(mail_user, main_pwd)
            smtp_obj.sendmail(sender, receivers, message.as_string())
            smtp_obj.quit()
            logger().info("邮件发送成功！")

        except smtplib.SMTPException as e:
            logger().error("Error:邮件发送失败，详情:{}".format(e))

    # 清空report目录功能
    def _del_temp_file(self):
        # 清空report目录，不然文件会堆积很多
        logger().info('删除临时目录')
        shutil.rmtree(settings.REPORT_PATH)
        logger().info("成功删除临时目录")


    def send_mail_msg(self):
        # 调用压缩功能
        self._compress_zip_file()
        # 调用发邮件操作
        self._send_mail()
        # 调用删除临时文件
        # self._del_temp_file()


if __name__ == "__main__":
    SendEmailHandler().send_mail_msg()
