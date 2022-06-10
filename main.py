def cucc():
    return "csirkefarhat"

def stg():
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium import webdriver

    browser = webdriver.Chrome(ChromeDriverManager().install())
    URL = "http://localhost:1667/"
    browser.get(URL)

    sign_up_btn = browser.find_element_by_xpath('.//a[@href="#/register"]')
    sign_up_btn.click()
    thing = browser.find_element_by_xpath('.//a[@href="#/login"]')
    if thing != '':
        return "yeah"
