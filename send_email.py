#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/4/17 10:29'


import os

import smtplib
from email.mime.text import MIMEText #纯文本邮件模板
from email.mime.multipart import MIMEMultipart #发送带附件



def send_email(file_new):

    #------------发件相关的参数------------------

    smtpserver     = "192.168.10.193" #发件服务器，自己配置
    port           = 25  #端口
    sender         = "xxoooxoxo@gz609.com" #账号，自己配置
    password       = "xxxxooooll" #密码
    # receiver     = "xxoxooxox@qq.com" #单个接收人
    receiver       = ["xxxxoooo@qq.com"]#多个收件人

    #-------------编辑邮件内容--------------------
    # 读文件
    with open(file_new,"rb") as fr:
        mail_body  = fr.read()
    msg            = MIMEMultipart()
    msg['From']    = sender                 #发件人
    msg['To']      = ";".join(receiver)      #多个收件人
    msg['Subject'] = "自动化运行结果" #主题


#正文
    body = MIMEText(mail_body,"html","utf-8")
    msg.attach(body)


#附件
    att = MIMEText(mail_body,_subtype='html',_charset="utf-8")
    att["Content-Type"]        = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)

#发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver) #连接服务器
        smtp.login(sender,password)#登录
    except Exception as er:
        smtp = smtplib.SMTP_SSL(smtpserver,port)
        smtp.login(sender,password)#登录
    smtp.sendmail(sender,receiver,msg.as_string())#发送
    smtp.quit()#关闭

def send_report(testreport):

    result_dir = testreport
    lists      = os.listdir(result_dir) #获取该目录下面的所有文件
    #找到最新生成的文件
    lists.sort(key=lambda fn:os.path.getmtime(result_dir+"\\"+fn))
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    #调用发邮件模块
    send_email(file_new)

def main_email():
    testreport = './report'
    send_report(testreport)

