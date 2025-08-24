from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from cloudinary.models import CloudinaryField


# models.py
from django.db import models
from django.core.mail import send_mail
from django.conf import settings
import random
import string
import json

class Order(models.Model):
    order_number = models.CharField(max_length=12, unique=True, editable=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    category = models.CharField(max_length=100, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    items_json = models.TextField()  # Will store all items as JSON
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.order_number:
            # Generate random order number (8 alphanumeric characters)
            self.order_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        super().save(*args, **kwargs)

    def get_items(self):
        return json.loads(self.items_json)

    def __str__(self):
        return f"Order {self.order_number}"

from django.db import models
from django.core.validators import MinLengthValidator

class Ticket(models.Model):
    TICKET_TYPES = [
        ('single', 'Entrada Individual'),
        ('season', 'Abono Temporada'),
    ]
    
    dni = models.CharField(max_length=20, validators=[MinLengthValidator(5)])
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    match = models.CharField(max_length=100)
    section = models.CharField(max_length=50)
    seat = models.CharField(max_length=10)
    purchase_date = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    qr_code = models.CharField(max_length=100, unique=True)
    ticket_type = models.CharField(max_length=10, choices=TICKET_TYPES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f"{self.full_name} - {self.match}"
    


# models.py
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Match(models.Model):
    # Match details
    date = models.DateTimeField()
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    
    # Team logos
    home_team_logo = CloudinaryField('image', folder='escudos')
    away_team_logo = CloudinaryField('image', folder='escudos')
    
    # Scores
    home_score = models.IntegerField(
        null=True, 
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
    away_score = models.IntegerField(
        null=True, 
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
    
    # Home/away flag
    is_olympia_home = models.BooleanField(default=True)
    
    # Location information
    location_name = models.CharField(max_length=200, blank=True)
    location_address = models.CharField(max_length=300, blank=True)
    maps_url = models.URLField(blank=True, verbose_name="Google Maps URL")
    
    # Additional info
    competition = models.CharField(max_length=100, blank=True)
    match_notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Matches"
    
    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.date.strftime('%Y-%m-%d')}"
    
    @property
    def has_played(self):
        return (self.date < timezone.now() and 
                self.home_score is not None and 
                self.away_score is not None)
    
    @property
    def result(self):
        if self.has_played:
            return f"{self.home_score} - {self.away_score}"
        return "TBD"
    
    @property
    def display_result(self):
        if self.has_played:
            if self.is_olympia_home:
                return f"{self.home_score} - {self.away_score}"
            else:
                return f"{self.away_score} - {self.home_score}"
        return "VS"
    
    @property
    def olympia_team(self):
        return self.home_team if self.is_olympia_home else self.away_team
    
    @property
    def olympia_logo(self):
        return self.home_team_logo if self.is_olympia_home else self.away_team_logo
    
    @property
    def opponent_team(self):
        return self.away_team if self.is_olympia_home else self.home_team
    
    @property
    def opponent_logo(self):
        return self.away_team_logo if self.is_olympia_home else self.home_team_logo
    
    @property
    def formatted_date(self):
        return self.date.strftime("%d %b %Y - %H:%Mh")
    
    @property
    def short_date(self):
        return self.date.strftime("%d/%m/%y")
    
    @property
    def is_future_match(self):
        return self.date > timezone.now() and self.home_score is None