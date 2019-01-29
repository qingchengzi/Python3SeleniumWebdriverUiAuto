#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2019/1/11 15:11'


from page.leadingendpage.achall_page import AcHall
from modules.common import LoginSuccess


class AcHallHandled():
    '''交流大厅页面的操作'''
    def __init__(self):
        self.obj_login = LoginSuccess()
        self.obj_acpage = AcHall()


    def login_achall_title(self):
        '''进入交流大厅'''
        rest_title = self.obj_acpage.achall_page("discuss/forum")
        flage = None
        print(rest_title)
        self.quit_driver()
        if rest_title=="xxooo大厅":
            flage = True
        return flage


    def post_a_message(self):
        '''通过modules中common.py中的LoginSuccess完成登录发帖功能'''
        return self.obj_login.post_a_message()


    def reply(self):
        '''交流大厅回帖'''
        return self.obj_login.reply_a_message()


    def like(self):
        '''帖子详情页面点赞'''
        return self.obj_login.random_like()


    def quit_driver(self):
        '''关闭浏览器窗口'''
        self.obj_acpage.outwebdriver() #关闭浏览器



if __name__ == '__main__':
    obj = AcHallHandled()
    obj.reply()