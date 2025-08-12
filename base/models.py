from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


def validate_unique_case_insensitive_username(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('Ya existe un usuario con ese nombre (sin distinguir mayúsculas/minúsculas).')

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_pack = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class UserService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quit_datetime = models.DateTimeField(default=timezone.now)  
    

    class Meta:
        unique_together = ('user', 'service')
    
    def __str__(self):
        return f"{self.user.username}'s {self.service.name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    services = models.ManyToManyField(Service, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

# Aplica tu validador personalizado al campo username del modelo User
UserProfile._meta.get_field('user').remote_field.model.username_validators = [validate_unique_case_insensitive_username]

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