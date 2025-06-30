from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    # Redirección principal
    path('', RedirectView.as_view(url='/home/', permanent=False)),
    
    # Páginas principales
    path('home/', views.home, name="home"),
    path('offline/', views.offline, name="offline"),
    path('inscripciones/', views.inscripciones_view, name='inscripciones'),
    path('cantera/', views.cantera_view, name='cantera'),
    path('download/', views.download_view, name='download'),
    path('about/', views.about_view, name='about'),
    
    # URLs PWA (sin duplicados)
    path('manifest.json', views.manifest, name='manifest'),
    path('sw.js', views.service_worker, name='service_worker'),
]

# Configuración de archivos estáticos SOLO en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)