# -*- coding:utf-8 -*-
"""
Python 3.7
Author：Spring
Time：  2022/3/29 5:05 PM

"""
import smtplib
import shutil
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.multipart import MIMEMultipart

class SendEmailTest():


    def send_email(self):


        # 第三方SMTP服务
        mail_host = 'smtp.exmail.qq.com'
        mail_user = 'fiona@myfriday.cn'
        mail_pwd = 'oGyuD4Jh9o2Pgs6W'

        sender = 'fiona@myfriday.cn'
        receivers = ['1517437552@qq.com']

        message = MIMEMultipart()

        # message = MIMEText('Python邮件发送测试...', 'plain', 'utf-8')
        message['From'] = Header("Spring", 'utf-8')
        message['To'] = Header("测试", 'utf-8')

        subject = 'Python STMP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        # 构造文字内容
        text = "Python邮件发送测试..."
        text_plain = MIMEText(text, 'plain', 'utf-8')
        message.attach(text_plain)  # 将文字内容添加到MIMEMultipart对象中

        # 构造图片链接
        sendimagefile = open(r"/Users/mac-mini/Downloads/1639134966888.jpg", 'rb').read()
        image = MIMEImage(sendimagefile)
        image.add_header('Content-ID', '<image1>')
        image['Content-Disposition'] = 'attachment; filename="testiamge.jpg"'
        message.attach(image)

        # 构造html
        html = """
        <html>
         <head></head>
         <body>
            <p>Hi!<br>
               How are you?<br>
               Here is the <a href="http://wwww.baidu.com">link</a>you wanted.<br>
            </p>
        </body>
        </html>
            
        """
        text_html = MIMEText(html, 'html', 'utf-8')
        text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
        message.attach(text_html)

        # shutil.make_archive('/Volumes/HDD/Code/Python/FridayDemo/Friday/App/ApiAuto/Debug/', "zip", root_dir='/Users/mac-mini/Downloads/1639134966888.jpg')

        # 构造附件
        sendfile = open(r'/Users/mac-mini/Downloads/allure-2.17.3.zip', 'rb').read()
        text_att = MIMEText(sendfile, 'base64', 'utf-8')
        text_att['Content-Type'] = 'application/octet-stream'
        text_att.add_header('Content-Disposition', 'attachment', filename='ceshi.zip')
        message.attach(text_att)

        try:

            smtpObj = smtplib.SMTP_SSL(mail_host)
            smtpObj.ehlo(mail_host)  # SMTP对象后，需要调用ehlo()方法，向SMTP电子邮件服务器“打招呼”，这是SMTP的第一步，对于建立到服务器的连接很重要
            # smtpObj.connect(mail_host, 465)
            smtpObj.login(mail_user, mail_pwd)
            smtpObj.sendmail(sender, receivers, message.as_string())

            print("邮件发送成功")

        except smtplib.SMTPException as e:
            print("Error:{}".format(e))

        smtpObj.quit()

if __name__ == '__main__':
    SendEmailTest().send_email()