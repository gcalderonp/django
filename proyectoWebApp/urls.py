from django.urls import URLPattern, path
from proyectoWebApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name ='home'),
    path('servicio/',servicio, name='servicios'),
    path('tienda/',tienda, name='tienda'),
    path('blog/',blog, name='blog'),
    path('contacto/',contacto, name='contacto'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)