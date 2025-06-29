from django.urls import path
from django.urls import include
from django.views.generic.base import RedirectView      
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=False)),  
    path('home/', views.home, name="home"),  
    path('register/', views.registerPage, name='register'), 
    path("offline/", views.offline, name="offline"),
    path('inscripciones/', views.inscripciones_view, name='inscripciones'),
    path('cantera/', views.cantera_view, name='cantera'),
    path('download/', views.download_view, name='download'),
    path('about/', views.about_view, name='about'),


]

