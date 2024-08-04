from django.shortcuts import render  # Import render function for rendering templates
from django.contrib import messages  # Import messages framework for displaying messages
from .models import Tool  # Import the Tool model from the current app


def tools_view(request):
    # Initialize context with an empty 'tools' list
    context = {
        'tools': [],
    }

    try:
        # Retrieve all tools from the database
        tools = Tool.objects.all()

        # Update the context with the retrieved tools
        context['tools'] = tools

    except Exception as e:
        # Add an error message to be displayed in the template
        messages.error(request, f'An error occurred: {str(e)}')

    # Render the 'tools_html/tools.html' template with the context
    return render(request, 'tools_html/tools.html', context)
