from selenium import webdriver
driver=webdriver.Firefox()
# Navigate to page stored as local file


driver.get("file:///home/athul/Documents/selenium-demo/button.html")

button=driver.find_element_by_id('default_btn')
webdriver.ActionChains(driver).click_and_hold(button).perform()