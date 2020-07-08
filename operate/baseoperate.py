from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from config.sysconfig import *
import sys
import time

class BaseOperate():
    operate_driver = webdriver.Chrome
    #创建一个构造函数 将driver传入
    def __init__(self,drvier):
        self.operate_driver = drvier
    def find_element(self,*loc):
        #封装find方法：接受元组类型，默认等待5s，寻找失败截图,:param loc:元组类型,必须是(By.NAME, 'username')这样的结构
        #:return:元素对象webelement
        try:
            webelement = WebDriverWait(self.operate_driver,5).until(lambda x:x.find_element(*loc))
            return webelement
        except (TimeoutException,NoSuchElementException) as e:
            ##寻找失败时自动截图至指定目录sreenshot，截图名称为调用方法名（测试用例名）+ 时间戳 + png后缀
            self.operate_driver.get_screenshot_as_file(SCREENSHOTURL+sys._getframe(1).f_code.co_name + time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))+".png")
    def click_element(self,*loc):
        #重封装的click方法，将寻找和点击封装到一起，适用于点击次数不多的元素
        try:
            webelement = self.find_element(*loc)
            webelement.click()
        except (TimeoutException,NoSuchElementException) as e:
            print('Error details :%s' % (e.msg))

    def is_page_has_text(self,text):
        #判断当前页面是否存在指定的文字
        #:param text:字符串类型，要判断是否存在的文字
        #:return:布尔值，True代表存在，False代表不存在
        nowtime = time.time()
        



