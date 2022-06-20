from user_data import *
import time


# A belépést megvalósító függvény
def login(obj):
    sign_in_btn = obj.find_element_by_xpath('.//a[@href="#/login"]')
    sign_in_btn.click()
    email_input = obj.find_element_by_xpath('.//input[@placeholder="Email"]')
    email_input.send_keys(users[0]['email'])
    pwd_input = obj.find_element_by_xpath('.//input[@placeholder="Password"]')
    pwd_input.send_keys(users[0]['password'])
    sign_in_btn = obj.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_btn.click()
    time.sleep(2)


# A regisztrációt megvalósító függvény
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
    time.sleep(2)


# Adott menüpontot kereső és arra kattintó függvény
def find_menu_item(obj, menu_point_name):
    login(obj)
    time.sleep(2)
    counter = 0
    navbar_buttons = obj.find_elements_by_xpath('//a[@class="nav-link"]')
    for i in navbar_buttons:
        if i.text == menu_point_name:
            break
        counter += 1
    navbar_buttons[counter].click()
    time.sleep(2)


# A sorozatos adatfeltöltésért felelős függvény, hibaellenőrzéssel kiegészítve
def data_upload(obj):
    login(obj)
    time.sleep(1)
    for i in range(0, len(new_articles)):
        new_article_btn = obj.find_element_by_xpath('.//a[@href="#/editor"]')
        new_article_btn.click()
        time.sleep(1)
        input_title = obj.find_element_by_xpath('//input[@placeholder="Article Title"]')
        input_about = obj.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]')
        textarea = obj.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]')
        input_tags = obj.find_element_by_xpath('//input[@placeholder="Enter tags"]')
        list_of_new_article_fields = [input_title, input_about, textarea, input_tags]
        counter = 0
        for key, value in new_articles[i].items():
            list_of_new_article_fields[counter].send_keys(value)
            counter += 1
        submit_btn = obj.find_element_by_xpath('//button[@type="submit"]')
        submit_btn.click()
        time.sleep(1)
        assert obj.find_element_by_xpath('//i[@class="ion-edit"]').is_displayed()


# Adott szerző bejegyzéseinek kigyűjtéséért felelős függvény
def find_author_articles(obj):
    time.sleep(2)
    find_authors = obj.find_elements_by_xpath('//a[@class="author"]')
    for i in find_authors:
        if users[0]['name'] == i.text:
            i.click()
            break
    time.sleep(1)


# Adott fájl esetén ellenőrzi, hogy van-e tartalma vagy nincs
def is_file_empty(file_name):
    with open(file_name, 'r', encoding='UTF-8') as f:
        first_char = f.read(1)
        if not first_char:
            return True
    return False
