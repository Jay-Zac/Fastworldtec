from django.apps import AppConfig  # Import the AppConfig class from django.apps


# Define a configuration class for the tools application
class ToolsConfig(AppConfig):
    # Specify the default field type for auto-generated primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    # Name of the application
    name = 'tools'
