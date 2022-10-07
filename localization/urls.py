from django.urls import path 
from . import views 

urlpatterns = [ 

    path('', views.index, name='index2'), 
    path('index/', views.index_oficial, name= 'index_oficial'),
    path('landing/', views.landing, name= 'landing'),
    path('reservar/',views.reservar, name='reservar' ),
    path('monitoring/',views.monitoring, name='monitoring' ),
    path('reservar/<str:sala>/<str:freserva>/',views.reservar, name='reservar' )


] 