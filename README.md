1、本系统使用了Python3+Unittest+HTMLTestRunner.py编写;

2、WebUi自动化测试系统，入口文件main_run.py;

3、config目录>settings.py文件为配置文件，将一些常量定义到文件中;

4、handled目录下面分为前台(leadingendhandled)目录和后台(adminhandled)目录，分别用来定义前台和后台的操作，handeld目录的作用
获取page目录中某个页面的结果然后进行逻辑判断，将判断结果返回到testcaseuite测试用例中;

5、log记录错误日志目录；

6、modules目录>common.py文件用来定义公共类，例如前后台登录成功的cookies，在有些页面需要携带登录成功后的cookies才能进一步操作；

7、page目录>base_page.py文件为Selenium中webdriver的具体操作，做为公共文件，每个页面通过继承base_page.py使用该文件中的方法,
page目录>adminpage目录和leadingendpaege目录中的.py文件定义了具体页面中xpath和css等的元素定位；

8、report测试报告目录;

9、test目录为自己写代码时可以先在该目录中写好，在移植到具体目录中;

10、testcaseuite目录具体测试用例目录，可以根据需求在划分目录，但是里面的.py文件必须是 test.py结尾;

11、send_email.py执行完毕后发邮件，里面根据提示填写收发邮件信息；
12、本次示例代码使用Google Chrome浏览器68.0.3440.75（正式版本）,ChromeDriver 2.42
