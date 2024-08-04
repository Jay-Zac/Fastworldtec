// Wait for the DOM content to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Get the contact form element
    const form = document.getElementById('contact-form');
    // Get the submit button inside the form
    const submitButton = form.querySelector('button[type="submit"]');
    // Variable to track if the form has changed
    let formChanged = false;

    // Add an event listener for input changes in the form
    form.addEventListener('input', () => {
        // Set formChanged to true when any input changes
        formChanged = true;
    });

    // Add an event listener for form submission
    form.addEventListener('submit', submitHandler);

    // Function to handle form submission
    function submitHandler(e) {
        // Prevent the default form submission behavior
        e.preventDefault();

        // Change the submit button text and disable it
        submitButton.textContent = 'Sending message, please wait...';
        submitButton.disabled = true;

        // Send the form data using fetch
        fetch(form.action, {
            method: 'POST',
            body: new FormData(form),
        })
        .then((response) => {
            // Check if the response is not ok
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // Return the response as JSON
            return response.json();
        })
        .then((data) => {
            // Check if the response message indicates success
            if (data.message === 'success') {
                // Alert the user of success and reset the form
                alert('Thank you for your message! We will get back to you soon.');
                form.reset();
                formChanged = false;
            } else {
                // Throw an error if the submission was not successful
                throw new Error('Submission was not successful! Please try again.');
            }
        })
        .catch((error) => {
            // Log the error and alert the user of a problem
            console.error('Error:', error);
            alert('There was a problem submitting your form. Please try again later.');
        })
        .finally(() => {
            // Reset the submit button text and enable it
            submitButton.textContent = 'Send Message';
            submitButton.disabled = false;
        });
    }

    // Add an event listener for before the window unloads
    window.addEventListener('beforeunload', (event) => {
        // Check if the form has been changed
        if (formChanged) {
            // Prevent the default unload behavior
            event.preventDefault();
            // Set the return value to display a confirmation dialog
            event.returnValue = '';
            return '';
        }
    });
});
