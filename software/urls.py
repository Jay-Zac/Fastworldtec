from django.urls import path  # Import path function for URL routing
from . import views  # Import views from the current app

# Define the application namespace for URL resolution
app_name = 'software'

urlpatterns = [
    # Define URL to map the 'software_view' function in views.py
    path('', views.software_view, name='software'),
]
