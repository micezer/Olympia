from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.urls import path
from . import views, webhooks
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Redirección principal
    path('', RedirectView.as_view(url='/home/', permanent=False)),
    
    # Páginas principales
    path('admin/', admin.site.urls),  # ✅ This line is required
    path('home/', views.home, name="home"),
    path('offline/', views.offline, name="offline"),
    path('shop/', views.shop_view, name='shop'),
    path('cantera/', views.cantera_view, name='cantera'),
    path('download/', views.download_view, name='download'),
    path('about/', views.about_view, name='about'),
    path('ticket/', views.ticket_purchase, name='ticket_purchase'),
    path('players/', views.get_players_by_team, name='get_players_by_team'),
    path('inscripcion/', views.inscripcion_view, name='inscripcion'),
    path('create-inscription/', views.create_inscription, name='create_inscription'),
    path('contactos/', views.contactos, name='contactos'),
    path('noticias/', views.news_view, name='news'),
    path('patrocinadores/', views.sponsors_view, name='sponsors'),
    path('copa_reina/', views.copa_view, name='copa_reina'),
    path('plantilla/', views.players_view, name='players'),
    path('api/players/', views.get_players_by_team, name='players_api'),








  






    
    # URLs PWA (sin duplicados)
    path('manifest.json', views.manifest, name='manifest'),
        path('serviceworker.js', views.serviceworker, name='serviceworker'),

]

# Configuración de archivos estáticos SOLO en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)