from django.urls import path
from . import views
urlpatterns = [
    path('', views.tour,name='tour'),
    path('add',views.submitform,name='submitform'),
]