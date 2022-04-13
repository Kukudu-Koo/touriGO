from django.urls import path
from . import views
urlpatterns = [
    path('', views.restaurants,name='restaurant'),
    path('add',views.submitform,name='submitform'),
]