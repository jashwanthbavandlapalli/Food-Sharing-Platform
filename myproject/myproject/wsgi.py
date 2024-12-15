"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
'''
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()
'''
import os
from django.core.wsgi import get_wsgi_application
from waitress import serve

# Set the default Django settings module for the 'wsgi' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the WSGI application for the project
application = get_wsgi_application()

# Run Waitress to serve the application
if __name__ == "__main__":
    serve(application, host='0.0.0.0', port=8000)

