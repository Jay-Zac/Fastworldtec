from django import forms  # Import forms module from Django
from .models import Course  # Import the Course model from the current app's models file


# Define a custom form class for the Course model
class CourseForm(forms.ModelForm):
    # Metaclass to specify the model and fields to use
    class Meta:
        # Specify the model to use for the form
        model = Course
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
                # Append "(Optional)" to the field label
                field.label = f'{field.label} (Optional field)'
            else:
                # Append "(Mandatory)" to the field label
                field.label = f'{field.label} (Mandatory field)'
