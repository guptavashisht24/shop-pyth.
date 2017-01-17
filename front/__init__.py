'''
set cache
'''
from datetime import date
from django.core.cache import cache

date_today = date.today().strftime("%d%m%Y")

if cache.get('today') is None or cache.get('today') != date_today:
    cache.set('today', date_today, None)
    cache.set('bill', 0, None)
    cache.set('description', 0, None)
    cache.set('sale', 0, None)
