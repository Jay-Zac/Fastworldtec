from django.db import models  # Import the models module from Django


# Homepage Software Section object
class HomepageSoftware(models.Model):
    objects = None  # Add to prevent unresolved attribute reference error in views.py in PYCHARM.

    # Field for storing an image, uploaded to 'homepage_software_images' directory
    image = models.ImageField(upload_to='homepage_software_images')

    # Field for the title of the software, with a maximum length of 255 characters
    title = models.CharField(max_length=255)

    # Field for the price of the software, optional, with a maximum length of 50 characters
    price = models.CharField(max_length=50, blank=True)

    # Field for a description of the software, optional, with no maximum length
    description = models.TextField(blank=True)

    # Field for storing an affiliate link, with a maximum length of 2083 characters
    affiliate_link = models.CharField(max_length=2083)

    # Field for storing the creation date and time, automatically set when an object is created
    date_and_time_created = models.DateTimeField(auto_now_add=True)

    # Meta class
    class Meta:
        # Order objects by creation date in descending order
        ordering = ('-date_and_time_created',)

        # Display name for the model in the admin portal
        verbose_name_plural = 'Homepage Software Only'

    # Method to return a string representation of the object
    def __str__(self):
        # Return title of the object
        return self.title


# Blog and Review Section Object
class BlogAndReview(models.Model):
    DoesNotExist = None  # Add to prevent unresolved attribute reference error in views.py in PYCHARM.
    objects = None  # Add to prevent unresolved attribute reference error in views.py in PYCHARM.

    # Field for storing an image, uploaded to 'blog_and_review_images' directory
    image = models.ImageField(upload_to='blog_and_review_images')

    # Field for the title of the blog or review, with a maximum length of 255 characters
    title = models.CharField(max_length=255)

    # Field for an excerpt or summary of the blog or review, with no maximum length
    excerpt = models.TextField()

    # Field for storing an affiliate link, optional, with a maximum length of 2083 characters
    affiliate_link = models.CharField(max_length=2083, blank=True)

    # Field for storing the creation date and time, automatically set when an object is created
    date_and_time_created = models.DateTimeField(auto_now_add=True)

    # Meta class
    class Meta:
        # Order objects by creation date in descending order
        ordering = ('-date_and_time_created',)

        # Display name for the model in the admin portal
        verbose_name_plural = 'Blogs & Reviews'

    # Method to return a string representation of the object
    def __str__(self):
        # Return title of the object
        return self.title


# Message Section Object
class Message(models.Model):
    # This line is redundant and should be removed, as it's not necessary
    objects = None

    # Field for the full name of the person sending the message, with a maximum length of 100 characters
    full_name = models.CharField(max_length=100)

    # Field for the email address of the person sending the message
    email = models.EmailField()

    # Field for the content of the message, with no maximum length
    message = models.TextField()

    # Field for storing the creation date and time, automatically set when an object is created
    date_created = models.DateField(auto_now_add=True)

    # Meta class
    class Meta:
        # Order objects by creation date in descending order
        ordering = ('-date_created',)
