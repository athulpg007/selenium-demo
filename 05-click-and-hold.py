from selenium import webdriver

driver=webdriver.Firefox()

# Direct to url
driver.get("http://www.apress.com")

# Locate 'Apress Access' web element button
button=driver.find_element_by_link_text("Account")

# Execute click-and-hold action on the element
webdriver.ActionChains(driver).click_and_hold(button).perform()