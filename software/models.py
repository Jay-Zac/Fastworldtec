from django.db import models  # Import the models module from django.db


# Software object
class Software(models.Model):
    objects = None  # Add to prevent unresolved attribute reference error in views.py in PYCHARM.

    # Image field to upload software images, storing them in 'all_software_images' directory
    image = models.ImageField(upload_to='all_software_images')

    # CharField for the software title with a maximum length of 255 characters
    title = models.CharField(max_length=255)

    # CharField for the software price with a maximum length of 50 characters, can be blank
    price = models.CharField(max_length=50, blank=True)

    # TextField for the software description, can be blank
    description = models.TextField(blank=True)

    # CharField for the affiliate link with a maximum length of 2083 characters
    affiliate_link = models.CharField(max_length=2083)

    # DateTimeField to store the date and time when the software was created, automatically set on creation
    date_and_time_created = models.DateTimeField(auto_now_add=True)

    # Metaclass to define metadata for the model
    class Meta:
        # Order software by date and time created in descending order
        ordering = ('-date_and_time_created',)

        # Change the plural name of the model in the admin portal
        verbose_name_plural = 'All Software'

    # Function to return the software title in admin portal
    def __str__(self):
        return self.title
