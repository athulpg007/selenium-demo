#Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()

driver.get('https://en.wikipedia.org/wiki/Apress')

ActionChains(driver)\
        .key_down(Keys.CONTROL)\
        .send_keys("a")\
        .key_up(Keys.CONTROL)\
        .key_down(Keys.CONTROL)\
        .send_keys("c")\
        .key_up(Keys.CONTROL)\
        .perform()

