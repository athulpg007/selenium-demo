import unittest
from selenium import webdriver

class Test(unittest.TestCase):
	
	def setUp(self):
		self.driver=webdriver.Firefox()
		print("Firefox Browser Opened")


	def test_apress(self):
		self.driver.get("https://apress.com")
		print("Apress")

	def test_google(self):
		self.driver.get("https://google.com")
		print("Google")

	def test_facebook(self):
		self.driver.get("https://facebook.com")
		print("Facebook")

	def test_twitter(self):
		self.driver.get("https://twitter.com")
		print("Twitter")

	def tearDown(self):
		self.driver.quit()
		print("Quit Browser")

if __name__ =="__main__":
	unittest.main()