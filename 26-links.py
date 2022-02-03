import requests
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://athulpg007.github.io/publications_cv.html")

links=driver.find_elements_by_css_selector("a")

for link in links:
	if (requests.head(link.get_attribute('href')).status_code==200):
		print(link.text+" ; "+"Link is Valid")
	else:
		print(link.text+" ; "+"Link is Invalid/Broken")