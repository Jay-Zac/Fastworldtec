from django.contrib import admin  # Import Django's admin module to register models
from .models import HomepageSoftware, BlogAndReview, Message  # Import models to register in the admin interface
from .forms import HomepageSoftwareForm, BlogAndReviewForm  # Import custom forms for HomepageSoftware and BlogAndReview
from django.db import models  # Imports the models module from Django's database
from django.forms import Textarea  # Imports the Textarea widget from Django's forms

# Register homepage models with the Django admin site


# Customize the Django admin site titles

# Set the title of the admin site (appears in browser tab)
admin.site.site_title = 'fastworldtec'

# Set the header title on the admin site pages
admin.site.site_header = 'fastworldtec Admin'

# Set the title of the index page (homepage) in the admin interface
admin.site.index_title = 'Admin'


# Define a custom admin class for the HomepageSoftware model
class HomepageSoftwareAdmin(admin.ModelAdmin):
    form = HomepageSoftwareForm  # Specify the form to use in the admin interface


# Register the HomepageSoftware model with the custom admin class
admin.site.register(HomepageSoftware, HomepageSoftwareAdmin)


# Define a custom admin class for the BlogAndReview model
class BlogAndReviewAdmin(admin.ModelAdmin):
    form = BlogAndReviewForm  # Specify the form to use in the admin interface


# Register the BlogAndReview model with the custom admin class
admin.site.register(BlogAndReview, BlogAndReviewAdmin)


class UserMessageAdmin(admin.ModelAdmin):
    # Sets a custom template for the change form view in the admin interface
    change_form_template = 'admin/change_form.html'

    # Specify the fields to display in the list view of the UserMessage model
    list_display = ('full_name', 'email', 'date_created',)

    # Make all fields read-only
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            # Return a list of fields that should be read-only
            return self.readonly_fields + ('full_name', 'email', 'message', 'date_created')
        # Return the default readonly fields if no object is being edited
        return self.readonly_fields

    # Allow deletion but no addition or change
    def has_add_permission(self, request):
        # Disallow addition of new objects
        return False

    def has_change_permission(self, request, obj=None):
        # Disallow changes to existing objects
        return False

    # Override the default form field for the message field to use a Textarea widget
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={'rows': 10, 'cols': 80, })},  # Set the dimensions of the textarea
    }


# Register the UserMessage model with the UserMessageAdmin customization
admin.site.register(Message, UserMessageAdmin)
