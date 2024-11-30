// Function to toggle between light and dark theme
function toggleTheme() {
    const body = document.body;
    const logo = document.getElementById('logo');
    const themeToggle = document.getElementById('theme-toggle');

    // Toggle the theme class on the body tag
    body.classList.toggle('dark-theme');

    // Update logo based on the theme
    if (body.classList.contains('dark-theme')) {
        logo.src = "{% static 'images/logo_dark.png' %}";  // Dark mode logo
        themeToggle.textContent = "🌙";  // Moon icon for dark theme
    } else {
        logo.src = "{% static 'images/logo_bright.png' %}";  // Light mode logo
        themeToggle.textContent = "☀️";  // Sun icon for light theme
    }
}

// Add event listener for theme toggle
document.getElementById('theme-toggle').addEventListener('click', toggleTheme);

// Initialize theme on page load
window.onload = function() {
    if (document.body.classList.contains('dark-theme')) {
        // If dark mode is active, set the dark logo and moon icon
        document.getElementById('logo').src = "{% static 'images/logo_dark.png' %}";
        document.getElementById('theme-toggle').textContent = "🌙"; // Moon icon
    } else {
        // Default to light mode
        document.getElementById('logo').src = "{% static 'images/logo_bright.png' %}";
        document.getElementById('theme-toggle').textContent = "☀️"; // Sun icon
    }
};
