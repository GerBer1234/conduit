import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import user_data
import random


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

        def teardown(self):
            self.browser.quit()

    def test_registration(self):
        random_user = random.randint(0, len(user_data.users))
        sign_in_btn = self.browser.find_element_by_xpath('.//a[@href="#/register"]')
        sign_in_btn.click()
        username = self.browser.find_element_by_xpath('.//input[@placeholder="Username"]')
        username.send_keys(user_data.users[random_user]['name'])
        email = self.browser.find_element_by_xpath('.//input[@placeholder="Email"]')
        email.send_keys(user_data.users[random_user]['email'])
        pwd = self.browser.find_element_by_xpath('.//input[@placeholder="Password"]')
        pwd.send_keys(user_data.users[random_user]['password'])
        sign_up_btn = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sign_up_btn.click()
        time.sleep(2)
        return_message = self.browser.find_element_by_xpath('.//div[@class="swal-title"]')
        try:
            assert return_message.text == 'Welcome!'
        except AssertionError:
            fail_msg = self.browser.find_element_by_xpath('.//div[@class="swal-text"]')
            print(f'A regisztráció meghiúsult! A hiba oka: {fail_msg.text}')
