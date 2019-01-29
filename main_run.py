#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/12/12 16:44'


import time
import unittest

from  HTMLTestRunner import HTMLTestRunner
import send_email



def runthe_test_case_set():
    '''运行测试用例集'''
    test_dir = './testcaseuite'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')
    return discover



if __name__ == '__main__':

    now       = time.strftime("%Y-%m-%d %H_%M_%S")
    now_title = time.strftime("%Y-%m-%d %H:%M")
    file_name = "{0}{1}{2}".format("./report/",now,'_result.html')
    with open(file_name,'wb') as wb:
        runnser = HTMLTestRunner(stream=wb,title="{0}web官网UI测试报告".format(now_title))
        runnser.run(runthe_test_case_set())

    send_email.main_email()