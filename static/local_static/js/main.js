// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling functionality for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        // Add a click event listener to each anchor link
        anchor.addEventListener('click', function (e) {
            // Prevent the default click action
            e.preventDefault();
            // Smoothly scroll to the target section
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Add an event listener for when the window has fully loaded
    window.addEventListener('load', () => {
        // Add a delay before adding the 'loaded' class to the body
        setTimeout(() => {
            document.body.classList.add('loaded');
        }, 500); // Delay of 500ms
    });

    // Cookie banner functionality
    // Get the cookie banner element
    const cookieBanner = document.getElementById('cookie-banner');
    // Get the accept cookies button element
    const acceptCookiesButton = document.getElementById('accept-cookies');
    // Get the reject cookies button element
    const rejectCookiesButton = document.getElementById('reject-cookies');

    // Function to set a cookie
    function setCookie(name, value, days) {
        // Initialize the expires string
        let expires = "";
        // If days are provided, set the expiration date
        if (days) {
            const date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        // Set the cookie with the name, value, and expiration date
        document.cookie = `${name}=${value || ""}${expires}; path=/`;
    }

    // Function to get a cookie by name
    function getCookie(name) {
        // Create the name=value string
        const nameEQ = `${name}=`;
        // Split the cookies into an array
        const ca = document.cookie.split(';');
        // Loop through the array of cookies
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i].trim();
            // If the cookie is found, return its value
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        // Return null if the cookie is not found
        return null;
    }

    // Function to hide the cookie banner
    function hideBanner() {
        cookieBanner.style.display = 'none';
    }

    // Function to handle the cookie choice
    function handleCookieChoice(accepted) {
        // Set the cookie choice
        setCookie('cookieChoice', accepted ? 'accepted' : 'rejected', 365);
        // Hide the cookie banner
        hideBanner();
        // Log the cookie choice
        console.log(`Cookies ${accepted ? 'accepted' : 'rejected'}`);
    }

    // Get the cookie choice from the cookies
    const cookieChoice = getCookie('cookieChoice');
    // If there is no cookie choice, show the cookie banner
    if (!cookieChoice) {
        cookieBanner.style.display = 'block';
    } else {
        // Handle the existing cookie choice
        handleCookieChoice(cookieChoice === 'accepted');
    }

    // Add event listener to the accept cookies button
    acceptCookiesButton.addEventListener('click', () => handleCookieChoice(true));
    // Add event listener to the reject cookies button
    rejectCookiesButton.addEventListener('click', () => handleCookieChoice(false));

// Theme switcher functionality
// Get the theme toggle button element
const themeToggle = document.getElementById('theme-toggle');
// Get the theme tooltip element
const themeTooltip = document.getElementById('theme-tooltip');
// Get the current theme span element
const currentThemeSpan = document.getElementById('current-theme');
// Array of available themes
const themes = ['light', 'dark', 'sepia'];
// Get the current theme index from localStorage or default to 'light'
let currentThemeIndex = themes.indexOf(localStorage.getItem('theme') || 'light');

// Set the current theme on the document
document.documentElement.setAttribute('data-theme', themes[currentThemeIndex]);
// Update the tooltip with the current theme
updateTooltip();
// Update the theme icons
updateThemeIcons();

// Add event listener to the theme toggle button
themeToggle.addEventListener('click', () => {
    // Cycle to the next theme
    currentThemeIndex = (currentThemeIndex + 1) % themes.length;
    // Get the new theme
    const newTheme = themes[currentThemeIndex];
    // Set the new theme on the document
    document.documentElement.setAttribute('data-theme', newTheme);
    // Save the new theme to localStorage
    localStorage.setItem('theme', newTheme);
    // Update the tooltip with the new theme
    updateTooltip();
    // Update the theme icons
    updateThemeIcons();
    // Show the tooltip
    showTooltip();
});

// Function to update the tooltip with the current theme
function updateTooltip() {
    currentThemeSpan.textContent = themes[currentThemeIndex].charAt(0).toUpperCase() + themes[currentThemeIndex].slice(1);
}

// Function to show the tooltip
function showTooltip() {
    themeTooltip.style.display = 'block';
    setTimeout(() => {
        themeTooltip.style.display = 'none';
    }, 2000);
}

// Function to update the theme icons
function updateThemeIcons() {
    document.querySelectorAll('.theme-icon').forEach(icon => {
        icon.style.opacity = '0.3';
    });
    const activeIcon = document.querySelector(`.${themes[currentThemeIndex]}-icon`);
    if (activeIcon) {
        activeIcon.style.opacity = '1';
    }
}

// Show the tooltip on hover
themeToggle.addEventListener('mouseenter', showTooltip);
// Hide the tooltip when the mouse leaves the button
themeToggle.addEventListener('mouseleave', () => {
    themeTooltip.style.display = 'none';
});

    // Message auto-hide and close button functionality
    // Select all elements with the class 'message'
    document.querySelectorAll('.message').forEach(message => {
        // Automatically hide each message after 5 seconds
        setTimeout(() => message.classList.add('fade-out'), 5000);

        // Find the close button within the message
        message.querySelector('.close-btn').addEventListener('click', () => {
            // Add the 'fade-out' class to hide the message when the close button is clicked
            message.classList.add('fade-out');
        });
    });

    // Back to Top button functionality
    // Get the Back to Top button element
    const backToTopButton = document.getElementById('back-to-top');
    // Variable to store the timeout for hiding the button
    let hideTimeout;
    // Variable to store the timeout for scroll debounce
    let scrollTimeout;

    // Function to show the Back to Top button
    function showBackToTopButton() {
        backToTopButton.classList.add('show');
        // Clear any existing hide timeout
        clearTimeout(hideTimeout);
        // Set a timeout to hide the button after 5 seconds
        hideTimeout = setTimeout(() => {
            backToTopButton.classList.remove('show');
        }, 5000);
    }

    // Add event listener for scrolling
    window.addEventListener('scroll', () => {
        // Show the button when the user scrolls down 100px from the top
        if (window.scrollY > 100) {
            showBackToTopButton();
        } else {
            // Hide the button when the user scrolls back to the top
            backToTopButton.classList.remove('show');
        }
        // Clear any existing scroll timeout
        clearTimeout(scrollTimeout);
        // Set a timeout to hide the button after 5 seconds of no scrolling
        scrollTimeout = setTimeout(() => {
            if (window.scrollY > 100) {
                backToTopButton.classList.remove('show');
            }
        }, 5000);
    });

    // Add event listener for the Back to Top button click
    backToTopButton.addEventListener('click', () => {
        // Smooth scroll to the top
        window.scrollTo({ top: 0, behavior: 'smooth' });
        showBackToTopButton();
    });

    // Show the button when the user touches the screen
    window.addEventListener('touchstart', showBackToTopButton);
});
// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling functionality for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        // Add a click event listener to each anchor link
        anchor.addEventListener('click', function (e) {
            // Prevent the default click action
            e.preventDefault();
            // Smoothly scroll to the target section
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Add an event listener for when the window has fully loaded
    window.addEventListener('load', () => {
        // Add a delay before adding the 'loaded' class to the body
        setTimeout(() => {
            document.body.classList.add('loaded');
        }, 500); // Delay of 500ms
    });

    // Cookie banner functionality
    // Get the cookie banner element
    const cookieBanner = document.getElementById('cookie-banner');
    // Get the accept cookies button element
    const acceptCookiesButton = document.getElementById('accept-cookies');
    // Get the reject cookies button element
    const rejectCookiesButton = document.getElementById('reject-cookies');

    // Function to set a cookie
    function setCookie(name, value, days) {
        // Initialize the expires string
        let expires = "";
        // If days are provided, set the expiration date
        if (days) {
            const date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        // Set the cookie with the name, value, and expiration date
        document.cookie = `${name}=${value || ""}${expires}; path=/`;
    }

    // Function to get a cookie by name
    function getCookie(name) {
        // Create the name=value string
        const nameEQ = `${name}=`;
        // Split the cookies into an array
        const ca = document.cookie.split(';');
        // Loop through the array of cookies
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i].trim();
            // If the cookie is found, return its value
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        // Return null if the cookie is not found
        return null;
    }

    // Function to hide the cookie banner
    function hideBanner() {
        cookieBanner.style.display = 'none';
    }

    // Function to handle the cookie choice
    function handleCookieChoice(accepted) {
        // Set the cookie choice
        setCookie('cookieChoice', accepted ? 'accepted' : 'rejected', 365);
        // Hide the cookie banner
        hideBanner();
        // Log the cookie choice
        console.log(`Cookies ${accepted ? 'accepted' : 'rejected'}`);
    }

    // Get the cookie choice from the cookies
    const cookieChoice = getCookie('cookieChoice');
    // If there is no cookie choice, show the cookie banner
    if (!cookieChoice) {
        cookieBanner.style.display = 'block';
    } else {
        // Handle the existing cookie choice
        handleCookieChoice(cookieChoice === 'accepted');
    }

    // Add event listener to the accept cookies button
    acceptCookiesButton.addEventListener('click', () => handleCookieChoice(true));
    // Add event listener to the reject cookies button
    rejectCookiesButton.addEventListener('click', () => handleCookieChoice(false));

    (function() {
    // Themes array
    const themes = ['light', 'dark', 'sepia']; // List of available themes
    // Default theme index
    let currentThemeIndex = 0; // Index of the current theme in the themes array

    // Get elements by their IDs
    const themeToggle = document.getElementById('theme-toggle'); // Element for toggling themes
    const currentThemeSpan = document.getElementById('current-theme'); // Element to display the current theme
    const themeTooltip = document.getElementById('theme-tooltip'); // Element for showing tooltip

    // Retrieve the saved theme from localStorage
    const savedTheme = localStorage.getItem('theme'); // Get the saved theme from localStorage
    if (savedTheme && themes.includes(savedTheme)) { // Check if the saved theme is valid
        // Apply the saved theme if it's valid
        currentThemeIndex = themes.indexOf(savedTheme); // Update the current theme index based on the saved theme
    }

    // Set the theme on the document
    document.documentElement.setAttribute('data-theme', themes[currentThemeIndex]); // Apply the current theme to the document

    // Function to update the tooltip with the current theme
    function updateTooltip() {
        if (currentThemeSpan) { // Check if the currentThemeSpan element exists
            const currentTheme = themes[currentThemeIndex]; // Get the current theme
            currentThemeSpan.textContent = currentTheme.charAt(0).toUpperCase() + currentTheme.slice(1); // Update tooltip text
        }
    }

    // Function to show the tooltip
    function showTooltip() {
        if (themeTooltip) { // Check if the themeTooltip element exists
            themeTooltip.style.display = 'block'; // Show the tooltip
            setTimeout(() => { // Set a timeout to hide the tooltip after 2 seconds
                themeTooltip.style.display = 'none'; // Hide the tooltip
            }, 2000);
        }
    }

    // Initial update of the tooltip with the current theme
    updateTooltip(); // Update the tooltip with the current theme on page load

    // Add event listener to the theme toggle button if it exists
    if (themeToggle) { // Check if the themeToggle element exists
        themeToggle.addEventListener('click', () => { // Add click event listener to toggle the theme
            // Cycle to the next theme
            currentThemeIndex = (currentThemeIndex + 1) % themes.length; // Move to the next theme index in a circular manner
            // Get the new theme
            const newTheme = themes[currentThemeIndex]; // Get the new theme
            // Set the new theme on the document
            document.documentElement.setAttribute('data-theme', newTheme); // Apply the new theme to the document
            // Save the new theme to localStorage
            localStorage.setItem('theme', newTheme); // Save the new theme to localStorage
            // Update the tooltip with the new theme
            updateTooltip(); // Update the tooltip text with the new theme
            // Show the tooltip
            showTooltip(); // Display the tooltip with the new theme
        });

        // Show the tooltip on hover
        themeToggle.addEventListener('mouseenter', showTooltip); // Show the tooltip when hovering over the theme toggle button

        // Hide the tooltip when the mouse leaves the button
        themeToggle.addEventListener('mouseleave', () => { // Add event listener to hide the tooltip when mouse leaves the button
            if (themeTooltip) { // Check if the themeTooltip element exists
                themeTooltip.style.display = 'none'; // Hide the tooltip
            }
        });
    }
})();


    // Message auto-hide and close button functionality
    // Select all elements with the class 'message'
    document.querySelectorAll('.message').forEach(message => {
        // Automatically hide each message after 5 seconds
        setTimeout(() => message.classList.add('fade-out'), 5000);

        // Find the close button within the message
        message.querySelector('.close-btn').addEventListener('click', () => {
            // Add the 'fade-out' class to hide the message when the close button is clicked
            message.classList.add('fade-out');
        });
    });

    // Back to Top button functionality
    // Get the Back to Top button element
    const backToTopButton = document.getElementById('back-to-top');
    // Variable to store the timeout for hiding the button
    let hideTimeout;
    // Variable to store the timeout for scroll debounce
    let scrollTimeout;

    // Function to show the Back to Top button
    function showBackToTopButton() {
        backToTopButton.classList.add('show');
        // Clear any existing hide timeout
        clearTimeout(hideTimeout);
        // Set a timeout to hide the button after 5 seconds
        hideTimeout = setTimeout(() => {
            backToTopButton.classList.remove('show');
        }, 5000);
    }

    // Add event listener for scrolling
    window.addEventListener('scroll', () => {
        // Show the button when the user scrolls down 100px from the top
        if (window.scrollY > 100) {
            showBackToTopButton();
        } else {
            // Hide the button when the user scrolls back to the top
            backToTopButton.classList.remove('show');
        }
        // Clear any existing scroll timeout
        clearTimeout(scrollTimeout);
        // Set a timeout to hide the button after 5 seconds of no scrolling
        scrollTimeout = setTimeout(() => {
            if (window.scrollY > 100) {
                backToTopButton.classList.remove('show');
            }
        }, 5000);
    });

    // Add event listener for the Back to Top button click
    backToTopButton.addEventListener('click', () => {
        // Smooth scroll to the top
        window.scrollTo({ top: 0, behavior: 'smooth' });
        showBackToTopButton();
    });

    // Show the button when the user touches the screen
    window.addEventListener('touchstart', showBackToTopButton);
});
