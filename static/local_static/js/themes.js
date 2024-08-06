// Wait for the DOM to fully load before running the script
document.addEventListener('DOMContentLoaded', () => {
    // Get the search input element
    const searchInput = document.getElementById('search-input');
    // Get the clear button element
    const clearButton = document.getElementById('clear-button');
    // Get the search button element
    const searchButton = document.querySelector('.search-button');
    // Get the container holding theme items
    const themesContainer = document.getElementById('themes-container');
    // Get all theme item elements within the container
    const themeItems = themesContainer.getElementsByClassName('product-page-detail-card');
    // Get the "No items available" message element
    const noResultsMessage = document.getElementById('no-results-message');

    // Function to filter theme items based on search input
    function filterThemes() {
        const query = searchInput.value.toLowerCase();
        let hasResults = false;

        Array.from(themeItems).forEach(item => {
            const title = item.getAttribute('data-title').toLowerCase();
            const description = item.getAttribute('data-description').toLowerCase();

            // Check if the title or description includes the search query
            if (title.includes(query) || description.includes(query)) {
                item.style.display = 'block'; // Show matching item
                hasResults = true;
            } else {
                item.style.display = 'none'; // Hide non-matching item
            }
        });

        // Display or hide the "No items available" message
        if (noResultsMessage) {
            noResultsMessage.style.display = hasResults ? 'none' : 'block';
        }

    }

    // Add event listener to search input for real-time filtering
    searchInput.addEventListener('input', filterThemes);

    // Add event listener to search button to trigger filtering on click
    searchButton.addEventListener('click', (event) => {
        event.preventDefault(); // Prevent default button behavior
        filterThemes(); // Trigger filtering on button click
    });

    // Add event listener to search input to trigger filtering on Enter key press
    searchInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault(); // Prevent default behavior
            filterThemes(); // Trigger filtering on Enter key press
        }
    });

    // Add event listener to clear button to reset search input and display
    clearButton.addEventListener('click', () => {
        searchInput.value = ''; // Clear search input
        filterThemes(); // Reset theme items display
    });
});
