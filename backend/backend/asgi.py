"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

#from channels.auth import AuthMiddlewareStack #추가
#from channels.routing import ProtocolTypeRouter, URLRouter #URLRouter 추가
from channels.routing import get_default_application
#from paint_game import routing
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

# application = ProtocolTypeRouter({
#   "http": get_asgi_application(),
#   "websocket": AuthMiddlewareStack( # 추가
#         URLRouter(
#             routing.websocket_urlpatterns
#         )
#     ),
# })
application = get_default_application()