from django.shortcuts import render  # Import render function for rendering templates
from django.contrib import messages  # Import messages framework for displaying messages
from .models import Theme  # Import the Theme model from the current app


def themes_view(request):
    # Initialize context with an empty 'themes' list
    context = {
        'themes': [],
    }

    try:
        # Retrieve all themes from the database
        themes = Theme.objects.all()

        # Update the context with the retrieved themes
        context['themes'] = themes

    except Exception as e:
        # Add an error message to be displayed in the template
        messages.error(request, f'An error occurred: {str(e)}')

    # Render the 'themes_html/themes.html' template with the context
    return render(request, 'themes_html/themes.html', context)
