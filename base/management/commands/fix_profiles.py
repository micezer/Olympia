# management/commands/fix_profiles.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from base.models import UserProfile

class Command(BaseCommand):
    help = 'Creates missing user profiles'

    def handle(self, *args, **options):
        for user in User.objects.all():
            if not hasattr(user, 'userprofile'):
                UserProfile.objects.create(user=user)
                self.stdout.write(f'Created profile for {user.username}')