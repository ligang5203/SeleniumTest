# coding: utf-8
# import re
# import os
import unittest
import HTMLTestRunner
from time import sleep
from selenium import webdriver
# from selenium_ActionChains import ActionChains


class MyTestCase(unittest.TestCase):
    def setUp(self):
        url = 'http://www.baidu.com'
        self.dr = webdriver.Firefox()
        self.dr.get(url)
        self.dr.implicitly_wait(20)
        self.dr.maximize_window()
        sleep(3)

    def test_1(self):
        test_url = "https://www.baidu/.com"
        self.assertFalse(self.dr.current_url == test_url)
        print "current url is: ", self.dr.current_url

    @unittest.skip(u"测试skip")
    def test_2(self):
        pass

    def tearDown(self):
        self.dr.quit()
        self.dr.close()
if __name__ == '__main__':
    filename = 'd:\\Report.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='selenium',
        description=u'展示测试结果'
        )
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_1"))
    suite.addTest(MyTestCase("test_2"))
    runner.run(suite)
