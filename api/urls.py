from django.urls import path
from .views import shorten_url, redirect_url

urlpatterns = [
    path('api/shorten/', shorten_url, name='shorten_url'),  
    path('<str:chave>/', redirect_url, name='redirect_url'), 
]
