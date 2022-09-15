import os 
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from localization.routing import ws_urlpatterns
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_spaces.settings') 

 
#declaramos los dos protocolos de conexiòn
application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket'  : AuthMiddlewareStack(URLRouter(ws_urlpatterns)) 
})