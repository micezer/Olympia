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
    list_display = ('home_team', 'away_team', 'date', 'matchday', 'competition', 'team_category')
    list_filter = ('date', 'competition', 'matchday', 'team_category')
    search_fields = ('home_team', 'away_team', 'competition')
    fieldsets = (
        (None, {
            'fields': ('team_category', 'date', 'home_team', 'away_team', 'matchday')
        }),
        ('Logos', {
            'fields': ('home_team_logo', 'away_team_logo')
        }),
        ('Scores', {
            'fields': ('home_score', 'away_score', 'is_olympia_home')
        }),
        ('Location', {
            'fields': ('location_name', 'location_address', 'maps_url')
        }),
        ('Additional Info', {
            'fields': ('competition', 'match_notes')
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


