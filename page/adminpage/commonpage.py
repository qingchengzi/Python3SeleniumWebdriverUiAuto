#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/12/17 18:11'

import time

from page import base_page

class AdminLogin(base_page.BasePage):

    def admin_login(self,*args,**kwargs):
        '''登录后台'''
        self.navigate(args[2])
        time.sleep(3)
        self.by_xpath(".//input[@id='username']").send_keys(args[0]) #输入用户名
        time.sleep(2)
        self.by_xpath(".//input[@id='userpass']").send_keys(args[1]) #输入密码
        time.sleep(2)
        self.by_css(".button-s").click() #点击登录
        time.sleep(2)
        login_cookie = self.get_cookie()
        return login_cookie





