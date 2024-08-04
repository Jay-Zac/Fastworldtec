from django.contrib import admin  # Import the admin module from Django
from .models import Theme  # Import the Theme model from the current app's models file
from .forms import ThemeForm  # Import the custom form class for Theme


# Define a custom admin class for the Theme model
class ThemeAdmin(admin.ModelAdmin):
    form = ThemeForm  # Specify the form to use in the admin interface


# Register the Theme model with the custom admin class
admin.site.register(Theme, ThemeAdmin)
