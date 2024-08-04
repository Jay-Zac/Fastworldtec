import os  # Import the os module to interact with the operating system

# Import the ASGI application getter function from Django
from django.core.asgi import get_asgi_application

# Set the default Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fastworldtec.settings')

# Get the ASGI application callable to serve the project
application = get_asgi_application()
