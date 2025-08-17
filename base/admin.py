from django.contrib import admin
from .models import Order, Ticket, UserProfile, Service

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Service)
admin.site.register(Order)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'dni', 'match', 'section', 'seat', 'purchase_date', 'is_used')
    list_filter = ('section', 'ticket_type', 'is_used')
    search_fields = ('full_name', 'dni', 'email')
    readonly_fields = ('purchase_date', 'qr_code')

admin.site.register(Ticket, TicketAdmin)
