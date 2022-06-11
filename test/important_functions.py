from user_data import *


def login(obj):
    sign_in_btn = obj.find_element_by_xpath('.//a[@href="#/login"]')
    sign_in_btn.click()
    email_input = obj.find_element_by_xpath('.//input[@placeholder="Email"]')
    email_input.send_keys(users[0]['email'])
    pwd_input = obj.find_element_by_xpath('.//input[@placeholder="Password"]')
    pwd_input.send_keys(users[0]['password'])
    sign_in_btn = obj.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_btn.click()
