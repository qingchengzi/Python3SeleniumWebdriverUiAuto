#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2018/12/13 17:41'


from config import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BasePage:

    def __init__(self):
        self.innerulr   = settings.INNERURL #内测url
        if settings.INTERFACE:
            self.driver = self.notinterface()
        else:
            self.driver = self.havetheinterface()


    def notinterface(self):
        '''浏览器无界面运行，正式运行时使用'''
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        return webdriver.Chrome(chrome_options=chrome_options)


    def havetheinterface(self):
        '''有界面运行，调试环境中使用'''
        chrome_driver = webdriver.Chrome()
        chrome_driver.maximize_window()
        return chrome_driver


    def navigate(self,url=None,path=None):
        '''ui打开web页面'''
        if url and path:
            url = "{0}{1}".format(url,path)
            self.driver.get(url)
        elif url :
            self.driver.get(url)
        else:
            self.driver.get(self.innerulr)


    def print_current_title(self):
        '''打印title'''
        return self.driver.title


    def print_current_url(self):
        '''打印url'''
        return self.driver.current_url


    def by_css(self,the_css):
        '''css定位'''
        return self.driver.find_element_by_css_selector(the_css)


    def bys_csss(self,the_csss):
        '''css复数形式定位'''
        return self.driver.find_elements_by_css_selector(the_csss)


    def by_xpath(self,the_xpath):
        '''xpath定位'''
        return self.driver.find_element_by_xpath(the_xpath)


    def bys_xpaths(self,the_xpaths):
        '''xpaths定位'''
        return self.driver.find_elements_by_xpath(the_xpaths)


    def by_tagename(self,the_tage):
        '''tag定位'''
        return self.driver.find_element_by_tag_name(the_tage)


    def bys_tagenames(self,the_tages):
        '''tag复数形式定位'''
        return self.driver.find_elements_by_tag_name(the_tages)


    def by_id(self,the_id):
        '''id定位'''
        return self.driver.find_element_by_id(the_id)


    def bys_ids(self,the_ids):
        '''id的复数形式定位'''
        return self.driver.find_elements_by_id(the_ids)


    def get_cookie(self):
        '''获取cookies'''
        return self.driver.get_cookies()


    def by_iframe(self,the_ifram):
        '''进入iframe'''
        return self.driver.switch_to_frame(the_ifram)


    def by_outifram(self):
        '''退出ifram'''
        return self.driver.switch_to_default_content()


    def outwebdriver(self):
        '''关闭浏览器'''
        return self.driver.quit()


    def switch_to_window_handles(self,index=0):
        '''在浏览器中打开多个选项卡时，切换浏览器选项卡的handles'''
        return self.driver.switch_to_window(self.driver.window_handles[index])


    def add_cookie(self,cookies=None,url=None):
        self.driver.get(url)
        self.driver.add_cookie(cookie_dict=cookies)




