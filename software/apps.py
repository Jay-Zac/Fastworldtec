from django.apps import AppConfig  # Import the AppConfig class from django.apps


# Configuration class for the software app
class SoftwareConfig(AppConfig):
    # Set the default auto field type to BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    # Define the name of the app
    name = 'software'
