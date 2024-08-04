from django.shortcuts import render  # Import render function for rendering templates
from django.contrib import messages  # Import messages framework for displaying messages
from .models import Software  # Import the Software model from the current app
from homepage.models import HomepageSoftware  # Import HomepageSoftware model from the homepage app


def software_view(request):
    try:
        # Retrieve the first four homepage software items from the database
        homepage_software = HomepageSoftware.objects.all()[0:4]
    except Exception as e:
        homepage_software = []
        messages.error(request, f'An error occurred while fetching homepage software: {str(e)}')

    try:
        # Retrieve all software from the database
        software = Software.objects.all()
    except Exception as e:
        software = []
        messages.error(request, f'An error occurred while fetching software: {str(e)}')

    # Combine software and homepage software
    all_software = list(homepage_software) + list(software)

    # Context library for all_software
    context = {
        'all_software': all_software
    }

    # Render the 'software_html/software.html' template with the context
    return render(request, 'software_html/software.html', context)
