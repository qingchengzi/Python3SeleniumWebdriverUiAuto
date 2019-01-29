#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2019/1/11 14:40'



#测试用例例子，实现发帖回帖点赞

import unittest

from handled.leadingendhandled.achall_handled import AcHallHandled



class AcHall(unittest.TestCase):
    '''发帖回帖点赞'''
    @classmethod
    def setUpClass(cls):
        cls.obj_ach = AcHallHandled()


    def test_01_loging_page(self):
        '''进入发帖页面'''
        rest = self.obj_ach.login_achall_title()
        self.assertTrue(rest)


    def test_02_posting(self):
        '''发布帖子成功'''
        rest = self.obj_ach.post_a_message()
        self.assertTrue(rest)


    def test_03_reply(self):
        '''回帖成功'''
        rest = self.obj_ach.reply()
        self.assertTrue(rest)


    def test_04_like(self):
        '''主题帖详情页，点赞'''
        rest = self.obj_ach.like()

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':

    unittest.main()