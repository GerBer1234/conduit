from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import user_data
import os

from important_functions import *


class TestConduit:
    def setup(self):
        # az Options osztály egy példányát hozzuk létre
        browser_options = Options()
        # a headless mód segítségével a felhasználói felület nélkül fut le a teszt
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        time.sleep(2)
        URL = main_url
        self.browser.get(URL)

    def test_registration(self):
        registration(self.browser)
        time.sleep(2)
        try:
            return_message = self.browser.find_element_by_xpath('.//div[@class="swal-title"]')
            assert return_message.text == return_messages[0]
        except AssertionError:
            fail_msg = self.browser.find_element_by_xpath('.//div[@class="swal-text"]')
            print(f'\nA regisztráció meghiúsult! A hiba oka: "{fail_msg.text}"!')

    def test_login(self):
        login(self.browser)
        time.sleep(2)
        try:
            settings_button = self.browser.find_element_by_xpath('.//a[@href="#/settings"]')
            assert settings_button.text == menu_items[0]
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
        find_menu_item(self.browser, menu_items[1])
        time.sleep(2)
        try:
            sign_up_btn = self.browser.find_element_by_xpath('.//a[@href="#/register"]')
            assert sign_up_btn.is_displayed()
        except AssertionError:
            print('A kijelentkezés nem sikerült!')

    def test_go_through_a_multi-page_list(self):
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
        find_menu_item(self.browser, menu_items[0])
        time.sleep(1)
        textarea = self.browser.find_element_by_xpath('//textarea[@placeholder="Short bio about you"]')
        textarea.clear()
        textarea.send_keys(user_data.bio_information)
        update = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        update.click()
        time.sleep(1)
        try:
            update_msg = self.browser.find_element_by_xpath('.//div[@class="swal-title"]')
            assert update_msg == return_messages[1]
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

    def test_serial_data_upload(self):
        data_upload(self.browser)

    def test_modify_data(self):
        find_menu_item(self.browser, ' Settings')
        time.sleep(1)
        input_profile_picture_url = self.browser.find_element_by_xpath('//input[@placeholder="URL of profile picture"]')
        try:
            if len(input_profile_picture_url.get_attribute('value')) != 0:
                input_profile_picture_url.clear()
                input_profile_picture_url.send_keys(profile_picture_url)
                update = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
                update.click()
            assert input_profile_picture_url.get_attribute('value') == profile_picture_url
        except AssertionError:
            print('A profilkép URL címének módosítása nem sikerült!')

    def test_delete_articles(self):
        data_upload(self.browser)
        home_btn = self.browser.find_element_by_xpath('.//a[@href = "#/"]')
        home_btn.click()
        find_author_articles(self.browser)
        number_of_articles = self.browser.find_elements_by_xpath('//div[@class="article-preview"]')
        length_of_list = len(number_of_articles)
        while length_of_list > 0:
            time.sleep(1)
            find_articles = self.browser.find_elements_by_xpath('//a[@class="preview-link"]')
            find_articles[0].click()
            time.sleep(1)
            delete_article_btn = self.browser.find_element_by_xpath('//button[@class="btn btn-outline-danger btn-sm"]')
            delete_article_btn.click()
            find_author_articles(self.browser)
            length_of_list -= 1
        try:
            assert find_author_articles(self.browser) is None
        except AssertionError:
            print('Nem sikerült a bejegyzések törlése!')

    def test_save_data(self):
        find_menu_item(self.browser, ' Settings')
        time.sleep(1)
        datas = [self.browser.find_element_by_xpath('//input[@placeholder="URL of profile picture"]'),
                 self.browser.find_element_by_xpath('//input[@placeholder="Your username"]'),
                 self.browser.find_element_by_xpath('//textarea[@placeholder="Short bio about you"]'),
                 self.browser.find_element_by_xpath('//input[@placeholder="Email"]'),
                 self.browser.find_element_by_xpath('//input[@placeholder="Password"]')]
        datas_length = 0
        with open('profile_data.txt', 'w', encoding='UTF-8') as f:
            for i in datas:
                f.write(i.get_attribute('placeholder')+': '+i.get_attribute('value'))
                f.write('\n')
        time.sleep(1)
        try:
            assert os.path.getsize('profile_data.txt') != 0
        except AssertionError:
            print('Az adatok fájlba mentése sikertelen!')

    def teardown(self):
        self.browser.quit()
