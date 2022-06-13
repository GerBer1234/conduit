from user_data import *
import time


def login(obj):
    sign_in_btn = obj.find_element_by_xpath('.//a[@href="#/login"]')
    sign_in_btn.click()
    email_input = obj.find_element_by_xpath('.//input[@placeholder="Email"]')
    email_input.send_keys(users[0]['email'])
    pwd_input = obj.find_element_by_xpath('.//input[@placeholder="Password"]')
    pwd_input.send_keys(users[0]['password'])
    sign_in_btn = obj.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_btn.click()


def registration(obj):
    sign_up_btn = obj.find_element_by_xpath('.//a[@href="#/register"]')
    sign_up_btn.click()
    username_input = obj.find_element_by_xpath('.//input[@placeholder="Username"]')
    username_input.send_keys(users[0]['name'])
    email_input = obj.find_element_by_xpath('.//input[@placeholder="Email"]')
    email_input.send_keys(users[0]['email'])
    pwd_input = obj.find_element_by_xpath('.//input[@placeholder="Password"]')
    pwd_input.send_keys(users[0]['password'])
    new_sign_up_btn = obj.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    new_sign_up_btn.click()


def find_menu_item(obj, menu_point_name):
    login(obj)
    time.sleep(2)
    counter = 0
    navbar_buttons = obj.find_elements_by_xpath('//a[@class="nav-link"]')
    print(len(navbar_buttons))
    for i in navbar_buttons:
        if i.text == menu_point_name:
            break
        counter += 1
    navbar_buttons[counter].click()

