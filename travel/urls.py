from django.urls import path
from . import views
urlpatterns = [
    path('', views.Travel,name='Travel'),
    path('add',views.submitform,name='submitform'),
]