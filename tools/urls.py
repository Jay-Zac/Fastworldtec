from django.urls import path  # Import the path function from django.urls
from . import views  # Import views from the current package

# Namespace for the tools app
app_name = 'tools'

# URL patterns for the tools app
urlpatterns = [
    # Define URL to map the tools_view function in views.py
    path('', views.tools_view, name='tools'),
]
