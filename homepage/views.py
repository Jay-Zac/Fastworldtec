from django.shortcuts import render  # Import the render function to render documents
from django.http import JsonResponse  # Import JsonResponse for sending JSON responses
from django.contrib import messages  # Import messages framework for displaying messages
from .models import HomepageSoftware, BlogAndReview, Message  # Import models for querying the database
from .forms import MessageForm  # Import the MessageForm for handling user messages


# View for homepage Software section, blog and review section
def homepage_view(request):
    try:
        # Retrieve the first four software items from the database
        homepage_software = HomepageSoftware.objects.all()[0:4]
    except Exception as e:
        # Set to an empty list in case of an error
        homepage_software = []

        # Display error message
        messages.error(request, f'An error occurred while retrieving software items: {str(e)}')

    try:
        # Retrieve all blog and review items from the database
        blog_and_review = BlogAndReview.objects.all()
    except Exception as e:
        # Set to an empty list in case of an error
        blog_and_review = []

        # Display error message
        messages.error(request, f'An error occurred while retrieving blog and review items: {str(e)}')

    # Handle POST requests to collect and save user messages
    if request.method == 'POST':
        # Instantiate the form with POST data
        form = MessageForm(request.POST)

        if form.is_valid():
            # Clean the form data
            cleaned = form.cleaned_data
            user_messages = Message(
                full_name=cleaned['full_name'],
                email=cleaned['email'],
                message=cleaned['message'],
            )
            try:
                # Save the message to the database
                user_messages.save()

                # Return a JSON response indicating success
                return JsonResponse({'message': 'success'})
            except Exception as e:
                # Display error message
                messages.error(request, f'An error occurred while saving your message: {str(e)}')
        else:
            # Display error message for invalid form data
            messages.error(request, 'Form data is not valid. Please check your input.')

    # For non-POST requests, instantiate an empty form
    form = MessageForm()

    # Prepare the context with software, blog and review data, and the form instance
    context = {
        # Add the retrieved software items to the context
        'homepage_software': homepage_software,
        # Add the retrieved blog and review items to the context
        'blog_and_review': blog_and_review,
        # Add the form instance to the context
        'form': form,

    }

    # Render the homepage template with the context data
    return render(request, 'homepage_html/homepage.html', context)


# Function to handle the detail view for a single blog and review post
def blog_and_review_detail_view(request, pk):
    try:
        # Retrieve the BlogAndReview object using the primary key (pk)
        blog_and_review = BlogAndReview.objects.get(id=pk)
    except BlogAndReview.DoesNotExist:
        # Set to None if the object does not exist
        blog_and_review = None

        # Display error message
        messages.error(request, 'The requested blog and review post does not exist.')
    except Exception as e:
        # Set to None in case of an error
        blog_and_review = None

        # Display error message
        messages.error(request, f'An error occurred while retrieving the blog and review post: {str(e)}')

        # Context dictionary to pass the retrieved blog and review object to the template
    context = {'blog_and_review': blog_and_review}

    # Render the 'blog_and_review_detail.html' template with the context
    return render(request, 'homepage_html/blog_and_review_detail.html', context)
