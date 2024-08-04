from django.contrib import admin  # Import the admin module from Django
from .models import Software  # Import the Software model from the current app's models file
from .forms import SoftwareForm  # Import the custom form class for Software


# Define a custom admin class for the Software model
class SoftwareAdmin(admin.ModelAdmin):
    form = SoftwareForm  # Specify the form to use in the admin interface


# Register the Software model with the custom admin class
admin.site.register(Software, SoftwareAdmin)
