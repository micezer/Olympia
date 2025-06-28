from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('', include('pwa.urls')),  # You MUST use an empty string as the URL prefix

]
