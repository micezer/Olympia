from django.contrib import admin
from .models import Order, Ticket

# Register your models here.

admin.site.register(Order)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'dni', 'match', 'section', 'seat', 'purchase_date', 'is_used')
    list_filter = ('section', 'ticket_type', 'is_used')
    search_fields = ('full_name', 'dni', 'email')
    readonly_fields = ('purchase_date', 'qr_code')

admin.site.register(Ticket, TicketAdmin)


# admin.py
from django.contrib import admin
from .models import Match
from .models import Player

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'short_date', 
        'home_team', 
        'away_team', 
        'home_score', 
        'away_score',
        'location_name',
        'is_olympia_home'
    )
    list_filter = ('date', 'is_olympia_home', 'competition')
    search_fields = ('home_team', 'away_team', 'location_name')
    date_hierarchy = 'date'
    fieldsets = (
        ('Match Details', {
            'fields': (
                'date', 
                'home_team', 
                'away_team', 
                'home_team_logo', 
                'away_team_logo',
                'is_olympia_home',
                'competition'
            )
        }),
        ('Scores', {
            'fields': ('home_score', 'away_score'),
            'classes': ('collapse',)
        }),
        ('Location', {
            'fields': ('location_name', 'location_address', 'maps_url')
        }),
        ('Additional Info', {
            'fields': ('match_notes',),
            'classes': ('collapse',)
        }),
    )

# admin.py
from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "team", "position", "number", "is_staff")
    list_filter = ("team", "position", "is_staff")
    search_fields = ("name", "full_name", "role")
