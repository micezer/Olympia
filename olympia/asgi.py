"""
ASGI config for goldness project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'olympia.settings')

application = get_asgi_application()

import os
from django.core.management import call_command
from django.db import connections
from django.db.utils import OperationalError

def load_fixtures_if_needed():
    try:
        cursor = connections['default'].cursor()
        cursor.execute("SELECT COUNT(*) FROM auth_user;")
        count = cursor.fetchone()[0]
        if count == 0:  # si no hay usuarios, carga la fixture
            call_command('load_initial_data')
    except OperationalError:
        # La DB no está lista, Django la migrará primero
        pass

load_fixtures_if_needed()
