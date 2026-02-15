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


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sponsors/')
    url = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name
    



from django.db import models

class Product(models.Model):
    # Tipos de producto
    CATEGORY_CHOICES = [
        ('clothing', 'Ropa'),
        ('footwear', 'Calzado'),
        ('merch', 'Merchandising'),
    ]
    
    # Información básica
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    
    # Imágenes
    image = models.ImageField(upload_to='shop/')
    image_hover = models.ImageField(upload_to='shop/', blank=True, help_text='Aparece al hacer hover')
    
    # Opciones de talla y color
    has_sizes = models.BooleanField(default=False, help_text='¿Tiene tallas?')
    has_colors = models.BooleanField(default=False, help_text='¿Tiene colores?')
    
    # Arrays guardados como texto simple (fácil de editar en admin)
    size_list = models.TextField(blank=True, help_text='Tallas separadas por comas. Ej: XS,S,M,L,XL o 36,37,38,39,40')
    color_list = models.TextField(blank=True, help_text='Colores separados por comas. Ej: Azul,Verde,Rojo')
    
    # Extras
    badge = models.CharField(max_length=50, blank=True, help_text='Ej: NUEVO, OFERTA')
    price_variant = models.CharField(max_length=100, blank=True, help_text='Ej: Diseño delante y detrás')
    stock = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.name} - {self.price}€"
    
    def get_size_list(self):
        """Convierte el texto en lista"""
        if self.size_list:
            return [s.strip() for s in self.size_list.split(',')]
        return []
    
    def get_color_list(self):
        """Convierte el texto en lista"""
        if self.color_list:
            return [c.strip() for c in self.color_list.split(',')]
        return []












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
    # Categoría del equipo (nuevo campo)
    TEAM_CATEGORY_CHOICES = [
        ('senior_a', 'Senior A - Primer Equipo'),
        ('senior_b', 'Senior B'),
        ('cantera', 'Cantera'),
        ('other', 'Otro'),
    ]
    
    team_category = models.CharField(
        max_length=20,
        choices=TEAM_CATEGORY_CHOICES,
        default='senior_a',
        verbose_name="Categoría del Equipo"
    )
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
    
    # Fixture information - ADD THIS FIELD ONLY
    matchday = models.PositiveIntegerField(
        null=True, 
        blank=True,
        verbose_name="Jornada",
        help_text="Número de jornada (ej: 1, 2, 3...)"
    )
    
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
    
    # ADD THIS PROPERTY FOR FIXTURE DISPLAY
    @property
    def fixture(self):
        """Returns the matchday in a display-friendly format"""
        if self.matchday:
            return f"J{self.matchday}"
        return ""
    
    # models.py
from django.db import models

class Player(models.Model):
    TEAM_CHOICES = [
        ('senior_a', 'Senior A - Primer Equipo'),
        ('senior_b', 'Senior B'),
        ('cantera', 'Cantera'),
    ]
    
    POSITION_CHOICES = [
        ('portero', 'Portera'),
        ('defensa', 'Defensa'),
        ('centrocampista', 'Centrocampista'),
        ('delantero', 'Delantera'),
        ('tecnico', 'Cuerpo Técnico'),
    ]
    
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200, blank=True)
    number = models.IntegerField()
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    display_position = models.CharField(max_length=50, blank=True)  # NUEVO CAMPO
    team = models.CharField(max_length=20, choices=TEAM_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, blank=True, default="")  # Cambiado a opcional
    image = CloudinaryField('image', blank=True, folder='escudos')
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.get_team_display()}"
    
    

from django.db import models
import uuid

class Inscription(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    birthdate = models.DateField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    
    # Sports Information
    CATEGORY_CHOICES = [
        ('Prebenjamín', 'Prebenjamín'),
        ('Benjamín', 'Benjamín'),
        ('Alevín', 'Alevín'),
        ('Infantil', 'Infantil'),
        ('Cadete', 'Cadete'),
        ('Juvenil', 'Juvenil'),
        ('Senior', 'Senior'),
    ]
    
    POSITION_CHOICES = [
        ('Portero', 'Portero'),
        ('Defensa', 'Defensa'),
        ('Centrocampista', 'Centrocampista'),
        ('Delantero', 'Delantero'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    experience = models.PositiveIntegerField(null=True, blank=True)
    previous_clubs = models.CharField(max_length=200, blank=True)
    medical_conditions = models.TextField(blank=True)
    
    # System fields
    inscription_number = models.CharField(max_length=10, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Hardcoded JSON data
    season = models.CharField(max_length=20, default="2023/2024")
    registration_fee = models.DecimalField(max_digits=6, decimal_places=2, default=150.00)
    included_items = models.TextField(
        default='[{"item": "Uniforme completo", "quantity": 1}, {"item": "Seguro médico", "quantity": 1}, {"item": "Acceso a instalaciones", "quantity": 1}]'
    )
    
    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.full_name} - {self.category} - {self.inscription_number}"
    
    def save(self, *args, **kwargs):
        if not self.inscription_number:
            self.inscription_number = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)
    
    def get_included_items(self):
        """Parse the included_items JSON string into Python objects"""
        import json
        try:
            return json.loads(self.included_items)
        except (json.JSONDecodeError, TypeError):
            return []
    
    def set_included_items(self, items_list):
        """Set included_items from a Python list"""
        import json
        self.included_items = json.dumps(items_list)