from django.conf.urls import url
from ferreted_away import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'contact/$', views.contact, name='contact'),
    url(r'sitemap/$', views.sitemap, name='sitemap'),
    url(r'login/$', views.login, name='login'),
    url(r'addaccount/$', views.addAccount, name='addAccount'),
    url(r'myaccount/$', views.myAccount, name='myAccount'),
    url(r'myaccount/myitems/$', views.myItems, name='myItems'),
    url(r'myaccount/additems/$', views.addItems, name='addItems'),
    url(r'myaccount/mywatchlist/$', views.myWatchlist, name='myWatchlist'),
    url(r'categories/$', views.categories, name='categories'),
	url(r'send_mail/$', views.send_message, name='sendMessage'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.showCategory,
        name='showCategory'),

    #url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<item_name_slug>[\w\-]+)/$',
    # views.showItem,
    # name='showItem'),


]