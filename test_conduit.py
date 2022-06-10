import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestConduit:
    def setup(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        URL = "http://localhost:1667/"
        self.browser.get(URL)

    def test_registration(self):
        sign_in_btn = self.browser.find_element_by_xpath('.//a[@href="#/register"]')
        sign_in_btn.click()
        username = self.browser.find_element_by_xpath('.//input[@placeholder="Username"]')
        username.send_keys('Béla')
        email = self.browser.find_element_by_xpath('.//input[@placeholder="Email"]')
        email.send_keys('bela1@bela.com')
        pwd = self.browser.find_element_by_xpath('.//input[@placeholder="Password"]')
        pwd.send_keys('A123456a')
        sign_up_btn = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sign_up_btn.click()
        time.sleep(2)
        return_message = self.browser.find_element_by_xpath('.//div[@class="swal-title"]')
        assert return_message.text == 'Registration failed!'
