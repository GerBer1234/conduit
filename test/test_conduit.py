from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import user_data

from important_functions import *


class TestConduit:
    def setup(self):
        # az Options osztály egy példányát hozzuk létre
        browser_options = Options()
        # a headless mód segítségével a felhasználói felület nélkül fut le a teszt
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        time.sleep(2)
        URL = "http://localhost:1667/"
        self.browser.get(URL)

    def test_registration(self):
        registration(self.browser)
        time.sleep(2)
        try:
            return_message = self.browser.find_element_by_xpath('.//div[@class="swal-title"]')
            assert return_message.text == 'Welcome!'
        except AssertionError:
            fail_msg = self.browser.find_element_by_xpath('.//div[@class="swal-text"]')
            print(f'\nA regisztráció meghiúsult! A hiba oka: "{fail_msg.text}"!')

    def test_login(self):
        login(self.browser)
        time.sleep(2)
        try:
            settings_button = self.browser.find_element_by_xpath('.//a[@href="#/settings"]')
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

    def test_logout(self):
        login(self.browser)
        time.sleep(2)
        counter = 0
        log_out_button = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')
        for i in log_out_button:
            if i.text == ' Log out':
                break
            counter += 1
        log_out_button[counter].click()
        time.sleep(2)
        try:
            sign_up_btn = self.browser.find_element_by_xpath('.//a[@href="#/register"]')
            sign_up_btn.click()
        except AssertionError:
            print('A kijelentkezés nem sikerült!')

    def test_data(self):
        login(self.browser)
        time.sleep(2)
        counter = 0
        pagination_list = self.browser.find_elements_by_xpath('//a[@class="page-link"]')
        for i in pagination_list:
            i.click()
            counter += 1
            time.sleep(1)
        try:
            assert counter == len(pagination_list)
        except AssertionError:
            print('Sajnos valami hiba adódott!')

    def test_new_data_to_profile(self):
        find_menu_item(self.browser, ' Settings')
        time.sleep(1)
        textare = self.browser.find_element_by_xpath('//textarea[@placeholder="Short bio about you"]')
        textare.clear()
        textare.send_keys(user_data.bio_information)
        update = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        update.click()
        try:
            update_msg = self.browser.find_element_by_xpath('.//div[@class="swal-title"]')
            assert update_msg == 'Update successful!'
        except AssertionError:
            print('A bio kitöltése sikertelen.')

    def test_listing_data(self):
        login(self.browser)
        time.sleep(1)
        find_authors = self.browser.find_elements_by_xpath('//a[@class="author"]')
        counter = 0
        for i in find_authors:
            if find_authors[0].text == i.text:
                counter += 1
        find_authors[0].click()
        time.sleep(1)
        try:
            list_of_titles = self.browser.find_elements_by_xpath('//h1')
            assert counter == len(list_of_titles)
        except AssertionError:
            print('Az adatok listázása nem volt megfelelő!')

    def teardown(self):
        self.browser.quit()
