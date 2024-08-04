from django.contrib import admin  # Import the admin module from Django
from .models import Tool  # Import the Tool model from the current app's models file
from .forms import ToolForm  # Import the custom form class for Tool


# Define a custom admin class for the Tool model
class ToolAdmin(admin.ModelAdmin):
    form = ToolForm  # Specify the form to use in the admin interface


# Register the Tool model with the custom admin class
admin.site.register(Tool, ToolAdmin)
