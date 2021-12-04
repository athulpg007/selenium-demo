from selenium import webdriver

driver = webdriver.Firefox()

#Open apress webpage
driver.get('https://apress.com')

#Set Window Size
driver.set_window_size(300,400)
print("Sets Browser Size")

driver.set_window_position(x=500,y=400)
print("Sets Browser Size")

driver.quit()