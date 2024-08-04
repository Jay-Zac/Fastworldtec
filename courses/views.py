from django.shortcuts import render  # Import render function for rendering templates
from django.contrib import messages  # Import messages framework for displaying messages
from .models import Course  # Import the Course model from the current app


def courses_view(request):
    # Initialize context with an empty 'courses' list
    context = {
        'courses': [],
    }

    try:
        # Retrieve all courses from the database
        courses = Course.objects.all()

        # Update the context with the retrieved courses
        context['courses'] = courses

    except Exception as e:
        # Add an error message to be displayed in the template
        messages.error(request, f'An error occurred: {str(e)}')

    # Render the 'courses_html/courses.html' template with the context
    return render(request, 'courses_html/courses.html', context)
