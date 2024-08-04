from django.contrib import admin  # Import Django's admin module to register models
from .models import HomepageSoftware, BlogAndReview, Message  # Import models to register in the admin interface
from .forms import HomepageSoftwareForm, BlogAndReviewForm  # Import custom forms for HomepageSoftware and BlogAndReview

# Register homepage models with the Django admin site


# Register the Message model
admin.site.register(Message)

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
