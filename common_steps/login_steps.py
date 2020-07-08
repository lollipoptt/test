# -*- coding: UTF-8 -*-
import unittest
import warnings
from selenium import webdriver
from time import sleep


class logintest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://stage.www.shanghaidisneyresort.com/en/")
    def tearDown(self):
        print('test end!')
    # @unittest.skipIf(3>2,"此用例不执行")
    def test_login1(self):
        #手机号密码错误
        self.driver.find_element_by_css_selector(".signIn").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("loginPageMobile").send_keys('1222')
        self.driver.find_element_by_id("loginPageMPassword").send_keys('abc')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector("span.pillSubmit").click()
        error_message=self.driver.find_element_by_css_selector("span.genericValidationErrorMessage").text
        self.assertEqual(error_message,"Your mobile number, email or password do not match our records; please reenter.")
    # @unittest.expectedFailure
    def test_login2(self):
            # 手机号密码正确
            self.driver.find_element_by_css_selector(".signIn").click()
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id("loginPageMobile").clear()
            self.driver.find_element_by_id("loginPageMobile").send_keys('17011111234')
            self.driver.find_element_by_id("loginPageMPassword").send_keys('test1234')
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_css_selector("span.pillSubmit").click()
            self.driver.implicitly_wait(10)
            correct_message=self.driver.find_element_by_css_selector(".signOut").text
            self.assertEqual(correct_message,"Sign Out")

    def test_login3(self):
        # 手机号密码为空
        self.driver.find_element_by_css_selector(".signIn").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector("span.buttonText").click()
        self.driver.implicitly_wait(10)


   