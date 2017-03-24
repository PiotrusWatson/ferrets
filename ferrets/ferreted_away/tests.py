from django.test import TestCase
from ferreted_away.models import *
"""
https://github.com/leifos/tango_with_django_19/blob/master/code/tango_with_django_project/rango/tests.py
"""

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
			
