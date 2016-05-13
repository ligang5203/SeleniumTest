# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("http://passport.kuaibo.com/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")

# 登陆快播私有云
driver.find_element_by_id("user_name").send_keys("username")
driver.find_element_by_id("user_pwd").send_keys("123456")
driver.find_element_by_id("dl_an_submit").click()
time.sleep(3)

# 定位到要右击的元素
qqq = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[2]")
# 对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(qqq).perform()


'''
#你也可以使用三行的写法，但我觉得上面两行写法更容易理解
chain = ActionChains(driver)
implement = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[2]")
chain.context_click(implement).perform()
'''

time.sleep(3)  # 休眠3秒
driver.close()

# 这里需要注意的是，在使用ActionChains 类之前，要先将包引入。
# 右击的操作会了，下面的其它方法比葫芦画瓢也能写出来。

# 鼠标双击的写法：

# 定位到要双击的元素
qqq = driver.find_element_by_xpath("xxx")
# 对定位到的元素执行鼠标双击操作
ActionChains(driver).double_click(qqq).perform()

# 鼠标拖放操作的写法:
#  定位元素的原位置
element = driver.find_element_by_name("source")
# 定位元素要移动到的目标位置
target = driver.find_element_by_name("target")

# 执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()