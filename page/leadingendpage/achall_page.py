#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2019/1/11 15:10'


import time

from page import base_page


class AcHall(base_page.BasePage):
    '''交流大厅页面'''

    def achall_page(self,path=None):
        '''进入交流大厅页面'''
        self.navigate(self.innerulr,path)
        return self.print_current_title()


    def login_post_details_page(self):
        self.by_xpath(".//*[@id='topic_all_content']/tr[1]/td[1]/a").click() #进入帖子详情页
        time.sleep(10)

