from django.test import TestCase, Client
from ferreted_away.models import *
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

class ModelTests(TestCase):

#populates the default database using the population script
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

#method to get a category by category name
	def get_category(self, name):
		from ferreted_away.models import Category
		try:
			cat = Category.objects.get(name=name)
		except Category.DoesNotExist:
			cat = None
		return cat

#tests if catgeory is added to the database		
	def test_if_category_added(self):
		cat = self.get_category('Transport')
		self.assertIsNotNone(cat)

#gets item by item name		
	def get_item(self, name):
		from ferreted_away.models import Item
		try:
			item = Item.objects.get(item_name=name)
		except Item.DoesNotExist:
			item = None
		return item

#tests if item added to database		
	def test_if_item_added(self):
		item = self.get_item('Rollerskates')
		self.assertIsNotNone(item)

#tests if item has views		
	def test_if_item_has_views(self):
		item = self.get_item('Rollerskates')
		item.views = 56
		item.save()
		self.assertEquals(item.views, 56)
	
#gets user by user name	
	def get_user(self, name):
		from django.contrib.auth.models import User
		try:
			user = User.objects.get(username=name)
		except User.DoesNotExist:
			user = None
		return user

#tets if user added to database		
	def test_is_user_added(self):
		user = self.get_user('fredrick')
		self.assertIsNotNone(user)

#gets item from watchlist by user		
	def get_watchlist(self, username):
		from ferreted_away.models import Watchlist
		try:
			watch = Watchlist.objects.get(user=username)
		except Watchlist.DoesNotExist:
			watch = None
		return watch

#gets comment from database by user		
	def get_comment(self, username):
		from ferreted_away.models import Comments
		try:
			comment = Comments.objects.get(user=username)
		except Comments.DoesNotExist:
			comment = None
		return comment
	
#check item added to watchlist
	def test_watchlist_is_added(self):
		wuser = self.get_user('fredrick')
		item = self.get_item('Batcave')
		w = Watchlist(item=item.itemId, user=wuser)
		w.save()
		watch = self.get_watchlist(wuser)
		self.assertIsNotNone(watch)

#tests comment is added		
	def test_comment_is_added(self):
		cuser = self.get_user('fredrick')
		item = self.get_item('Batcave')
		c = Comments(user=cuser, item=item, comment='words')
		c.save()
		comment = self.get_comment(cuser)
		self.assertIsNotNone(comment)

class ViewsTests(TestCase):

#populates database with population script
	def setUp(self):
		self.client = Client()
		try:
			from population_script import populate
			populate()
		except ImportError:
			print('The module population_script does not exist')
		except NameError:
			print('The function populate() does not exist')
		except:
			print('Undisclosed error')

#gets item by item name
	def get_item(self, name):
		from ferreted_away.models import Item
		try:
			item = Item.objects.get(item_name=name)
		except Item.DoesNotExist:
			item = None
		return item
	
#tests home page loads	
	def test_home_load_correctly(self):
		response = self.client.get(reverse('home'))
		self.assertEquals(response.status_code, 200)
	
#test about page loads	
	def test_about_load_correctly(self):
		response = self.client.get(reverse('about'))
		self.assertEquals(response.status_code, 200)

#test faq page loads		
	def test_faq_load_correctly(self):
		response = self.client.get(reverse('faq'))
		self.assertEquals(response.status_code, 200)

#tests contact page loads correctly		
	def test_contact_load_correctly(self):
		response = self.client.get(reverse('contact'))
		self.assertEquals(response.status_code, 200)

#tests sitemap loads correctly		
	def test_sitemap_load_correctly(self):
		response = self.client.get(reverse('sitemap'))
		self.assertEquals(response.status_code, 200)

#tests login page loads correctly		
	def test_login_load_correctly(self):
		response = self.client.get(reverse('login'))
		self.assertEquals(response.status_code, 200)

#tests logout wont load if user not logged in		
	def test_logout_wont_load_if_not_logged_in(self):
		response = self.client.get(reverse('logout'))
		self.assertEquals(response.status_code, 302)

#tests add account loads correctly		
	def test_addaccount_load_correctly(self):
		response = self.client.get(reverse('addAccount'))
		self.assertEquals(response.status_code, 200)

#tests my account wont load if not logged in		
	def test_myaccount_wont_load_if_not_logged_in(self):
		response = self.client.get(reverse('myAccount'))
		self.assertEquals(response.status_code, 302)

#tests my items wont load if not logged in		
	def test_myitems_wont_load_if_not_logged_in(self):
		response = self.client.get(reverse('myItems'))
		self.assertEquals(response.status_code, 302)

#tests add item wont load if not logged in		
	def test_additem_wont_load_if_not_logged_in(self):
		username = 'fredrick'
		response = self.client.get(reverse('addItems', args=[username]))
		self.assertEquals(response.status_code, 302)

#tests my watchlist cant be accessed if not logged in		
	def test_mywatchlist_wont_load_if_not_logged_in(self):
		response = self.client.get(reverse('myWatchlist'))
		self.assertEquals(response.status_code, 302)

#tests category loads correctly		
	def test_category_load_correctly(self):
		response = self.client.get(reverse('categories'))
		self.assertEquals(response.status_code, 200)

#tests show category page loads correctly		
	def test_showcategory_load_correctly(self):
		response = self.client.get(reverse('showCategory', args=['Transport']))
		self.assertEquals(response.status_code, 200)

#tests item page loads correctly		
	def test_item_load_correctly(self):
		item = self.get_item('Private Jet')
		id = item.itemId
		response = self.client.get(reverse('showItem', args=[id]))
		self.assertEquals(response.status_code, 200)

#tests price range page loads correctly		
	def test_pricerange_load_correctly(self):
		response = self.client.get(reverse('priceRange', args=[0]))
		self.assertEquals(response.status_code, 200)

#tests browse by price range loads correctly		
	def test_browseprice_load_correctly(self):
		response = self.client.get(reverse('browsePrice'))
		self.assertEquals(response.status_code, 200)

#test cant delete item if not logged in		
	def test_delete_wont_load_if_not_logged_in(self):
		item = self.get_item('Private Jet')
		id = item.itemId
		response = self.client.get(reverse('deleteItem', args=[id]))
		self.assertEquals(response.status_code, 302)

#test cant add to watchlist if not logged in		
	def test_addwatchlist_wont_load_if_not_logged_in(self):
		item = self.get_item('Private Jet')
		id = item.itemId
		response = self.client.get(reverse('addWatchlist', args=[id]))
		self.assertEquals(response.status_code, 302)

#tets cant remove from watchlist if not logged in		
	def test_removewatchlist_wont_load_if_not_logged_in(self):
		item = self.get_item('Private Jet')
		id = item.itemId
		response = self.client.get(reverse('removeWatchlist', args=[id]))
		self.assertEquals(response.status_code, 302)

#tests search results page loads correctly		
	def test_searchresults_load_correctly(self):
		response = self.client.get(reverse('searchresults'))
		self.assertEquals(response.status_code, 200)

#tests google-manadated verify page loads correctly		
	def test_verify_load_correctly(self):
		response = self.client.get(reverse('verify'))
		self.assertEquals(response.status_code, 200)

	
		
	
	
		
	
		
	
		
	
			
