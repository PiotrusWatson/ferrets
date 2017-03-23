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
