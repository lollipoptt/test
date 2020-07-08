#encoding: utf-8
import time

from behave import *

from features.utils.seleniumapi import SeleniumApi


@given('open SHDR website URL')
def step_open(self):
    SeleniumApi.step_startup(self)

@when('input {username} and {passward} and click login')
def step_login(self,username,passward):
    time.sleep(1)
    SeleniumApi.step_send_keys(self,_mobile_field,passward)
    SeleniumApi.step_send_keys(self)