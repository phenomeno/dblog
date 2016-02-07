"""
WSGI config for dblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dblog.settings")

_application = get_wsgi_application()

def application(environ, start_response):
    os.environ["POSTGRESQL_NAME"] = environ.get("POSTGRESQL_NAME")
    os.environ["POSTGRESQL_USER"] = environ.get("POSTGRESQL_USER")
    os.environ["POSTGRESQL_PASSWORD"] = environ.get("POSTGRESQL_PASSWORD")
    os.environ["POSTGRESQL_HOST"] = environ.get("POSTGRESQL_HOST")
    return _application(environ, start_response)
