from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.views.generic.base import RedirectView      
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=False)),  
    path('home/', views.home, name="home"),  
    path("offline/", views.offline, name="offline"),  # Essential for PWA offline page
    path('inscripciones/', views.inscripciones_view, name='inscripciones'),
    path('cantera/', views.cantera_view, name='cantera'),
    path('download/', views.download_view, name='download'),
    path('about/', views.about_view, name='about'),
    path('manifest.json', views.manifest, name='manifest'),

]

# Service Worker URL - Important for PWA
urlpatterns += [
    path('sw.js', views.service_worker, name='service_worker'),
    path('manifest.json', views.manifest, name='manifest'),
]

# Static files during development (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)