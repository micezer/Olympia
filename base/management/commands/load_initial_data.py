from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Load initial fixture data into the database'

    def handle(self, *args, **options):
        fixture_path = os.path.join('myapp', 'fixtures', 'db_dump.json')
        self.stdout.write(f'Loading fixture: {fixture_path}')
        call_command('loaddata', fixture_path)
        self.stdout.write(self.style.SUCCESS('Fixture loaded successfully'))
