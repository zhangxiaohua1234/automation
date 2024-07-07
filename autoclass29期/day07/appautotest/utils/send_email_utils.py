#  -*- coding:utf-8 -*-
"""
作者：张德宝
日期：2023年09月03日
"""
import yagmail


class SEND_EMAIL:
    def __init__(self, sender, passwd, host, accpet, subject, context, attach, cc):
        self.sender = sender #发送方
        self.passwd = passwd #发送方密码
        self.host = host     #发送的邮箱域名
        self.accpet = accpet #接收方
        self.subject = subject #邮件主题
        self.context = context #邮件内容
        self.attach = attach   #附件
        self.cc = cc  #抄送
    def send(self):
        #初始化邮件服务
        email_server = yagmail.SMTP(user=self.sender, password=self.passwd,
                                    host=self.host)
        #发送邮件
        email_server.send(to=self.accpet,
                          subject=self.subject,
                          contents=self.context,
                          # attachments=self.attach,
                          cc=self.cc)