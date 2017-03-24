from django.test import TestCase
from ferreted_away.models import *
from django.urls import reverse

class ModelTests(TestCase):
	def setUp(self):
		try:
			from population_script import populate
			populate()
		except ImportError:
			print('The module population_script does not exist')
		except NameError:
			print('The function populate() does not exist')
		except:
			print('Undisclosed error')

	def get_category(self, name):
		from ferreted_away.models import Category
		try:
			cat = Category.objects.get(name=name)
		except Category.DoesNotExist:
			cat = None
		return cat
		
	def test_if_category_added(self):
		cat = self.get_category('Transport')
		self.assertIsNotNone(cat)
		
	def get_item(self, name):
		from ferreted_away.models import Item
		try:
			item = Item.objects.get(item_name=name)
		except Item.DoesNotExist:
			item = None
		return item
	
	def test_if_item_added(self):
		item = self.get_item('Rollerskates')
		self.assertIsNotNone(item)
		
	def test_if_item_has_views(self):
		item = self.get_item('Rollerskates')
		item.views = 56
		item.save()
		self.assertEquals(item.views, 56)
		
	def get_user(self, name):
		from django.contrib.auth.models import User
		try:
			user = User.objects.get(username=name)
		except User.DoesNotExist:
			user = None
		return user
		
	def test_is_user_added(self):
		user = self.get_user('fredrick')
		self.assertIsNotNone(user)
		
class ViewsTests(TestCase):	
	def test_home_load_correctly(self):
		response = self.client.get(reverse('home'))
		self.assertEquals(response.status_code, 200)
	
	def test_about_load_correctly(self):
		response = self.client.get(reverse('about'))
		self.assertEquals(response.status_code, 200)
		
	def test_faq_load_correctly(self):
		response = self.client.get(reverse('faq'))
		self.assertEquals(response.status_code, 200)
		
	def test_contact_load_correctly(self):
		response = self.client.get(reverse('contact'))
		self.assertEquals(response.status_code, 200)
		
	def test_sitemap_load_correctly(self):
		response = self.client.get(reverse('sitemap'))
		self.assertEquals(response.status_code, 200)
		
	def test_login_load_correctly(self):
		response = self.client.get(reverse('login'))
		self.assertEquals(response.status_code, 200)
		
	def test_logout_wont_load_if_not_logged_in(self):
		response = self.client.get(reverse('logout'))
		self.assertEquals(response.status_code, 302)
		
	def test_addaccount_load_correctly(self):
		response = self.client.get(reverse('addAccount'))
		self.assertEquals(response.status_code, 200)
		
	def test_myaccount_wont_load_if_not_logged_in(self):
		response = self.client.get(reverse('myAccount'))
		self.assertEquals(response.status_code, 302)
		
	
		
	
		
	
			
