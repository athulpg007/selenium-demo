from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://apress.com')

#Open Google page
driver.get('https://google.com')
#Go back to previous 'apress' page

driver.back()
print("Moved to first page")

#Go to current page
driver.forward()
print("Moved to second page")

driver.refresh()

print("Page is Refreshed")