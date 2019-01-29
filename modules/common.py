#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/12/12 16:44'

import sys
import os

from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings

error_path    = settings.LOG_PATH #日志路径


def write_error_log(content):
    '''将错误信息写入日志'''
    _content  ="\n{0}:{1}".format(datetime.now().strftime("%Y-%m-%d %X"),content)
    _filename = os.path.join(error_path,'errorlog.log')
    with open(_filename,'a+',encoding='utf-8') as fa:
        fa.write(_content)


class CommonClass():
    '''公共类'''
    def __init__(self):
        #后台登录地址、用户名和密码
        self.adminuser = settings.ADMINUSER
        self.adminpad  = settings.ADMINPASS
        self.admin_url = settings.ADMINURL  #内测后台url
        self.admin_success_cookie = self.login_admin()#后台登录成功后的cookes

    def login_admin(self):
        '''登录后台'''
        pass


class LoginSuccess:
    '''内测和线上登录成功后，获取登录成功后的cookies'''

    def __init__(self):
        self.close_url = settings.INNERURL    #内测url
        self.username  = settings.PRIVATEUSER #内测前台账号
        self.password  = settings.PASSWORD    #内测前台密码
        self.private_login_cookie = self.login_page() #内测登录成功后的cookies


    def login_page(self):
        '''登录成功后台的cookies且返回'''
        pass



if __name__ == '__main__':

    obj = LoginSuccess()
