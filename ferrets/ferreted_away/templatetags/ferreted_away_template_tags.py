from django import template
from ferreted_away.models import Category

register = template.Library()

@register.inclusion_tag('ferrets/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(),
             'act_cat':cat}