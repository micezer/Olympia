from django.contrib import admin
from .models import Order

# Register your models here.

from.models import UserProfile
from .models import Service

admin.site.register(UserProfile)
admin.site.register(Service)


admin.site.register(Order)