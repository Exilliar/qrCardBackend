from django.contrib import admin

from .models import Account, Card, Stat, CardStats

# Register your models here.

admin.site.register(Account)
admin.site.register(Card)
admin.site.register(Stat)
admin.site.register(CardStats)
