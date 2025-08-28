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
    path('inscripcion/', views.inscripcion_view, name='inscripcion'),
    path('tienda/', views.tienda_view, name='tienda'),
    path('cantera/', views.cantera_view, name='cantera'),
    path('download/', views.download_view, name='download'),
    path('about/', views.about_view, name='about'),
    path('enviar-email/', views.formulario_inscripcion, name='enviar_email'),
    path('create-order/', views.create_order, name='create_order'),
    path('ticket/', views.ticket_purchase, name='ticket_purchase'),
    path('purchase/', views.purchase_ticket, name='purchase_ticket'),
    path('tickets/', views.get_tickets, name='get_tickets'),
    path('api/players/', views.get_players_by_team, name='get_players_by_team'),
    path('inscripcion/', views.registration_form, name='registration_form'),
    path('check-existing-registration/', views.check_existing_registration, name='check_existing_registration'),
    path('save-registration/', views.save_registration, name='save_registration'),
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),
    path('test-csrf/', views.test_csrf, name='test_csrf'),
    path('complete-registration/', views.complete_registration, name='complete_registration'),
    path('check-payment-eligibility/', views.check_payment_eligibility, name='check_payment_eligibility'),









    
    # URLs PWA (sin duplicados)
    path('manifest.json', views.manifest, name='manifest'),
        path('serviceworker.js', views.serviceworker, name='serviceworker'),

]

# Configuración de archivos estáticos SOLO en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)