"""Try to use selenium with Safari browser

https://webkit.org/blog/6900/webdriver-support-in-safari-10/

/usr/bin/safaridriver --enable


SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

label.sendKeys(Keys.PAGE_DOWN);

driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

driver.implicitly_wait(30) # seconds

body = browser.find_element_by_css_selector('body')
body.send_keys(Keys.PAGE_DOWN)

"""
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


SCROLL_PAUSE_TIME = 1.0

browser = webdriver.Safari()
# URL = 'https://pypi.org/project/selenium/'
# URL = 'https://www.youtube.com/watch?v=WddpRmmAYkg'
# URL = 'https://twitter.com/bitcoin'
URL = 'https://twitter.com/search?q=bitcoin'
try:
    browser.get(URL)
    # last_height = browser.execute_script("return document.body.scrollHeight")
    # print(last_height)
    # time.sleep(SCROLL_PAUSE_TIME)
    # browser.execute_script("window.scrollTo(0, window.scrollY + 200)")

    # browser.execute_script("window.scrollTo(0, 2500)")
    # last_height = browser.execute_script("return document.body.scrollHeight")
    # time.sleep(SCROLL_PAUSE_TIME)
    # browser.execute_script("window.scrollTo(0, window.scrollY + 200)")

    # browser.execute_script("window.scrollTo(0, 2500)")
    # last_height = browser.execute_script("return document.body.scrollHeight")
    # print(last_height)

    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "article"))
    )
    print(element)
    # body = browser.find_element_by_css_selector('body')
    # body.send_keys(Keys.PAGE_DOWN)
    # data = browser.page_source
    # with open('data.txt', 'w') as fp:
    #     fp.write(data)
    # for _ in range(0):
    #     time.sleep(2.0)
    #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #     # body.send_keys(Keys.ARROW_DOWN)
    #     # body.send_keys(Keys.PAGE_DOWN)

    # time.sleep(SCROLL_PAUSE_TIME)
finally:
    time.sleep(5.0)
    browser.quit()
    pass
