# coding: utf-8
from selenium import webdriver
import time

# 模拟登陆163邮箱
dr = webdriver.Firefox()
dr.get("http://mail.163.com")
dr.implicitly_wait(10)
print "current title is:", dr.title
dr.maximize_window()
time.sleep(2)
dr.find_element_by_id('idInput').click()
dr.find_element_by_id('idInput').clear()
time.sleep(1)
dr.find_element_by_id('idInput').send_keys('userID')
dr.find_element_by_id('pwdInput').click()
dr.find_element_by_id('pwdInput').clear()
time.sleep(1)
dr.find_element_by_id('pwdInput').send_keys('passWD')
dr.find_element_by_id('loginBtn').submit()
dr.implicitly_wait(10)
print "current title is:", dr.title
time.sleep(5)

# dr.switch_to.alert().accept() 切换到alert弹窗
'''
将滚动条移动到页面的顶部
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)

将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
'''
# dr.find_element_by_id("user_name").send_keys(Keys.TAB)
# selenium2 python在send_keys()中输入中文一直报错，其实前面加个小u 就解决了：send_keys(u"输入中文")
