# coding: utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
'''
cookie = driver.get_cookies()  # 获得cookie信息
print cookie  # 将获得cookie的信息打印
driver.quit()
'''
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])
