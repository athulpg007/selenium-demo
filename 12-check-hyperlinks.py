import requests
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://apress.com/")
links=driver.find_elements_by_css_selector("a")

for link in links:
	if (requests.head(link.get_attribute('href')).status_code==200):
		print("Link is Valid")
	else:
		print("Link is Invalid/Broken")