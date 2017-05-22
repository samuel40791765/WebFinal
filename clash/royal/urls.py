from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^deck/', views.deck,name='deck'),
    url(r'^card_rank/', views.card_rank,name='card_rank'),
    url(r'^generic/', views.generic,name='generic'),
    
 ]