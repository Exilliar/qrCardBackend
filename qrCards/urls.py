from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/<str:accountEmail>',
         views.getAccountId, name='getAccount'),
    path('account/<int:accountid>/card', views.card, name='card')
]
