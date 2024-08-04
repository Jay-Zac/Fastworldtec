import os  # Import the os module for interacting with the operating system

from django.core.wsgi import get_wsgi_application  # Import get_wsgi_application for WSGI application setup

# Set the default Django settings module for the 'django-admin' command
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fastworldtec.settings')

# Get the WSGI application for the project
application = get_wsgi_application()
