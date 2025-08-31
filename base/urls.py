from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Redirección principal
    path('', RedirectView.as_view(url='/home/', permanent=False)),
    
    # Páginas principales
    path('admin/', admin.site.urls),  # ✅ This line is required
    path('home/', views.home, name="home"),
    path('offline/', views.offline, name="offline"),
    path('tienda/', views.tienda_view, name='tienda'),
    path('cantera/', views.cantera_view, name='cantera'),
    path('next-match/', views.get_next_match, name='next_match_api'),
    path('download/', views.download_view, name='download'),
    path('about/', views.about_view, name='about'),
    path('create-order/', views.create_order, name='create_order'),
    path('ticket/', views.ticket_purchase, name='ticket_purchase'),
    path('purchase/', views.purchase_ticket, name='purchase_ticket'),
    path('tickets/', views.get_tickets, name='get_tickets'),
    path('players/', views.get_players_by_team, name='get_players_by_team'),
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),
    path('inscripcion/', views.inscripcion_view, name='inscripcion'),
    path('create-inscription/', views.create_inscription, name='create_inscription'),



  






    
    # URLs PWA (sin duplicados)
    path('manifest.json', views.manifest, name='manifest'),
        path('serviceworker.js', views.serviceworker, name='serviceworker'),

]

# Configuración de archivos estáticos SOLO en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)