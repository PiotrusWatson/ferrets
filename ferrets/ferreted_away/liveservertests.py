from django.test import TestCase, Client
from ferreted_away.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

		
class MySeleniumTests(StaticLiveServerTestCase):
	fixtures = ['user_data.json']
	
	@classmethod
	def setUpClass(cls):
		super(MySeleniumTests, cls).setUpClass()
		cls.selenium = WebDriver()
		cls.selenium.implicilty_wait(10)
	
	@classmethod
	def tearDownClass(cls):
		cls.selenium.quit()
		super(MySeleniumTests, cls).tearDownClass()
		
	def test_login(self):
		self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
		username_input = self.selenium.find_element_by_name("username")
		username_input.send_keys('myuser')
		password_input = self.selenium.find_element_by_name("password")
		password_input.send_keys('secret')
		self.selenium.find_element_by_xpath('//input[@value="Log In"]').click()
