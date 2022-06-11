import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import user_data
import random

random_user = random.randint(0, len(user_data.users) - 1)
username = user_data.users[random_user]['name']
email = user_data.users[random_user]['email']
password = user_data.users[random_user]['password']


class TestConduit:
    def setup(self):
        # az Options osztály egy példányát hozzuk létre
        browser_options = Options()
        # a headless mód segítségével a felhasználói felület nélkül fut le a teszt
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        time.sleep(6)
        URL = "http://localhost:1667/"
        self.browser.get(URL)
        time.sleep(6)

    def test_registration(self):
        sign_up_btn = self.browser.find_element_by_xpath('.//a[@href="#/register"]')
        sign_up_btn.click()
        username_input = self.browser.find_element_by_xpath('.//input[@placeholder="Username"]')
        username_input.send_keys(username)
        email_input = self.browser.find_element_by_xpath('.//input[@placeholder="Email"]')
        email_input.send_keys(email)
        pwd_input = self.browser.find_element_by_xpath('.//input[@placeholder="Password"]')
        pwd_input.send_keys(password)
        sign_up_btn = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sign_up_btn.click()
        time.sleep(2)

        try:
            return_message = self.browser.find_element_by_xpath('.//div[@class="swal-title"]')
            assert return_message.text == 'Welcome!'
        except AssertionError:
            fail_msg = self.browser.find_element_by_xpath('.//div[@class="swal-text"]')
            print(f'\nA regisztráció meghiúsult! A hiba oka: "{fail_msg.text}"!')

    def test_login(self):
        sign_in_btn = self.browser.find_element_by_xpath('.//a[@href="#/login"]')
        sign_in_btn.click()
        email_input = self.browser.find_element_by_xpath('.//input[@placeholder="Email"]')
        email_input.send_keys(email)
        pwd_input = self.browser.find_element_by_xpath('.//input[@placeholder="Password"]')
        pwd_input.send_keys(password)
        sign_in_btn = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sign_in_btn.click()
        time.sleep(2)
        try:
            settings_button = self.browser.find_element_by_xpath('.//a[@href="#/settings"]')
            print(settings_button.text)
            assert settings_button.text == ' Settings'
        except AssertionError:
            print(f'\nA belépés sikertelen!')

    def test_cookie(self):
        cookie_accept_btn = self.browser.find_element_by_xpath('//button[@class="cookie__bar__buttons__button '
                                                               'cookie__bar__buttons__button--accept"]')
        cookie_accept_btn.click()
        try:
            time.sleep(2)
            cookie_bar_content = self.browser.find_elements_by_id("cookie-policy-panel")
            assert len(cookie_bar_content) == 0
        except AssertionError:
            print('A sütik elfogadása nem sikerült!')

    def teardown(self):
        self.browser.quit()
