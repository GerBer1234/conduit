def cucc():
    return "csirkefarhat"

import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

browser = webdriver.Chrome(ChromeDriverManager().install())
URL = "http://localhost:1667/"
browser.get(URL)