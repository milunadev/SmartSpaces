
from .consumers import *
from django.urls import path

 
ws_urlpatterns = [ 
    path('ws/consumer1/',WSConsumer.as_asgi()),
    path('ws/laboratorio/',WSConsumer_laboratorio.as_asgi()),
 ]