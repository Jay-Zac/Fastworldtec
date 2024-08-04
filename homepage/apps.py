from django.apps import AppConfig  # Import the AppConfig class from Django


# Define a configuration class for the homepage application
class HomepageConfig(AppConfig):
    # Set the default field type for auto-generated primary keys
    default_auto_field = 'django.db.models.BigAutoField'

    # Specify the name of the application
    name = 'homepage'
