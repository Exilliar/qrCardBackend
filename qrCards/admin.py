from django.contrib import admin

from .models import Account, Card, Stat, AccountCards, CardStats

# Register your models here.

admin.site.register(Account)
admin.site.register(Card)
admin.site.register(Stat)
admin.site.register(AccountCards)
admin.site.register(CardStats)
