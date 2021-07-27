"""
WSGI config for Maktab_52_Django_Clothing_Store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Maktab_52_Django_Clothing_Store.settings')

application = get_wsgi_application()
