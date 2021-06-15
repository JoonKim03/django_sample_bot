"""
WSGI config for sample_bot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample_bot.settings')

sys.path.append('/home/ubuntu/django/django_sample_bot')
sys.path.append('/home/ubuntu/django/myvenv/lib/python3.8/site-packages')

application = get_wsgi_application()

