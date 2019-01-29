#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/12/12 16:44'

import os

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_PATH  = os.path.join(BASE_DIR,'log') #日志目录

#是否启用浏览器界面，调试阶段需要启用浏览器的界面，正常运行就不需要浏览器界面,False是启用浏览器

INTERFACE = True


INNERURL    = "192.168.10.32:8001" #内测前台
ADMINURL    = "192.168.10.32:888"  #内测后台
ADMINUSER   = "admin"  #后台管理员账号
ADMINPASS   = "123456" #后台管理员密码

PRIVATEUSER = "test001"#前台账号
PASSWORD    = "123456" #前台密码


