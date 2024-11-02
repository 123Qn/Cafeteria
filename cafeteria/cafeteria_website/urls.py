from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dessert',views.desert, name='dessert'),
    path('drink',views.drink, name='drink'),
    path('dining',views.dining, name='dining')
    
]