from django.urls import path 
from . import views 

urlpatterns = [ 

    path('', views.index, name='index2'), 
    path('index/', views.index_oficial, name= 'index_oficial'),
    path('landing/', views.landing, name= 'landing'),


] 