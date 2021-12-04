import unittest
from selenium import webdriver

class Test(unittest.TestCase):

	@classmethod
	def setUpClass(suc):
		suc.driver=webdriver.Firefox()
		print("Open Browser using setUpClass method")


	def setUp(self):
		print("Exexute Setup")


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
		print("Execute teardown")

	@classmethod
	def tearDownClass(suc):
		suc.driver.quit()
		print("Close Browser using tearDownClass method")

if __name__ =="__main__":
	unittest.main()