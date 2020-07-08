#coding: utf-8
_author_ = 'teenie'
import sys
from behave import *
from selenium import webdriver

def before_all(context):
    reload(sys)
    sys.setdefaultencoding('utf-8')

def before_feature(context):
    context.driver = webdriver.Chrome()

def after_feature(context):
    context.driver.quit()
