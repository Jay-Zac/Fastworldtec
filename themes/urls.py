from django.urls import path  # Import the path function from django.urls
from . import views  # Import views from the current package

# Namespace for the themes app
app_name = 'themes'

# URL patterns for the themes app
urlpatterns = [
    # Define url to map the themes_view function in views.py
    path('', views.themes_view, name='themes'),
]
