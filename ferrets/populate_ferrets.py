import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferrets.settings')

import django
django.setup()
from rango.models import Category, Item, 