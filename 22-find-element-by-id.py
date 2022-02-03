from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Firefox()
# Navigate to page stored as local file


driver.get("file:///home/athul/Documents/Codes/selenium-demo/employee.html")

Employee_form = driver.find_element(By.ID, 'EmployeeForm')
