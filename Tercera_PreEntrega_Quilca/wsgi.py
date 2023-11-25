"""
WSGI config for Tercera_PreEntrega_Quilca project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tercera_PreEntrega_Quilca.settings')

application = get_wsgi_application()
