from django import forms  # Import the forms module from Django
from .models import Message  # Import the Message model from the current application
from .models import HomepageSoftware  # Import the HomepageSoftware model from the current app's models file
from .models import BlogAndReview  # Import the BlogAndReview model from the current app's models file


# Define a form based on the Message model
class MessageForm(forms.ModelForm):
    class Meta:
        # Specify the model that the form is based on
        model = Message
        # Specify the fields to include in the form
        fields = ('full_name', 'email', 'message',)


# Define a custom form class for the HomepageSoftware model
class HomepageSoftwareForm(forms.ModelForm):
    # Metaclass to specify the model and fields to use
    class Meta:
        # Specify the model to use for the form
        model = HomepageSoftware
        # Include all fields from the model
        fields = '__all__'

    # Initialize the form
    def __init__(self, *args, **kwargs):
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)
        # Iterate over each field in the form
        for field_name, field in self.fields.items():
            # Get the corresponding model field
            model_field = self._meta.model._meta.get_field(field_name)
            # Check if the model field is optional
            if model_field.blank or model_field.null:
                # Append "(Optional field)" to the field label
                field.label = f'{field.label} (Optional field)'
            else:
                # Append "(Mandatory field)" to the field label
                field.label = f'{field.label} (Mandatory field)'


# Define a custom form class for the BlogAndReview model
class BlogAndReviewForm(forms.ModelForm):
    # Metaclass to specify the model and fields to use
    class Meta:
        # Specify the model to use for the form
        model = BlogAndReview
        # Include all fields from the model
        fields = '__all__'

    # Initialize the form
    def __init__(self, *args, **kwargs):
        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)
        # Iterate over each field in the form
        for field_name, field in self.fields.items():
            # Get the corresponding model field
            model_field = self._meta.model._meta.get_field(field_name)
            # Check if the model field is optional
            if model_field.blank or model_field.null:
                # Append "(Optional field)" to the field label
                field.label = f'{field.label} (Optional field)'
            else:
                # Append "(Mandatory field)" to the field label
                field.label = f'{field.label} (Mandatory field)'
