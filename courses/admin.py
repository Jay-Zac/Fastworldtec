from django.contrib import admin  # Import the admin module from Django
from .models import Course  # Import the Course model
from .forms import CourseForm  # Import the CourseForm


# Define a custom ModelAdmin class for the Course model
class CourseAdmin(admin.ModelAdmin):
    # Specify the custom form to use in the admin interface
    form = CourseForm


# Register the Course model with the custom CourseAdmin class
admin.site.register(Course, CourseAdmin)
