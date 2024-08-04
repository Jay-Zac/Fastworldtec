from django.urls import path  # Import the path function from django.urls
from . import views  # Import views from the current package

# Namespace for the courses app
app_name = 'courses'

# URL patterns for the courses app
urlpatterns = [
    # Define url to map the 'courses_view' function in views.py
    path('', views.courses_view, name='courses'),
]
