"""
WSGI config for simplemooc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simplemooc.settings')

#application = get_wsgi_application() #Comentado para a alteração abaixo

#HEROKU
from dj_static import Cling
application = Cling(get_wsgi_application())