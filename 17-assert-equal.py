import unittest
from selenium import webdriver

class test_case1(unittest.TestCase):
	
	def test1(self):
		
		driver=webdriver.Firefox()
		driver.get("https://apress.com")
		title1 =driver.title
		title2 ="Apress Home"
		# Verifying Page Title
		self.assertEqual(title1, title2, "Title Page do not Match.")

if __name__ =="__main__":
	unittest.main()