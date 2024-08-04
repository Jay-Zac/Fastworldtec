// Wait for the DOM to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {
    // Select key elements from the DOM
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    // Function to toggle the navigation menu
    function toggleNav() {
        // Toggle the 'nav-active' class on the nav element
        nav.classList.toggle('nav-active');
        // Toggle the 'toggle' class on the burger element
        burger.classList.toggle('toggle');

        // Add animation to each nav link
        navLinks.forEach((link, index) => {
            // If the link already has an animation, remove it
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                // Add the fade-in animation with a slower, more staggered delay for each link
                link.style.animation = `navLinkFade 1s ease forwards ${index / 5 + 0.5}s`;
            }
        });
    }

    // Add click event listener to the burger menu
    burger.addEventListener('click', toggleNav);

    // Add click event listeners to each nav link
    navLinks.forEach(link => {
        link.addEventListener('click', toggleNav);
    });

    // Add click event listener to the entire document
    document.addEventListener('click', function(event) {
        // Check if the click is inside the nav or on the burger
        const isClickInsideNav = nav.contains(event.target);
        const isClickOnBurger = burger.contains(event.target);

        // If the click is outside nav and burger, and the nav is active, close the nav
        if (!isClickInsideNav && !isClickOnBurger && nav.classList.contains('nav-active')) {
            toggleNav();
        }
    });
});