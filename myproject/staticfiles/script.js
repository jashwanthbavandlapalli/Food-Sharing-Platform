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

const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Toggle dark mode
themeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
});

// Function to open the donation form
function openDonationForm() {
    document.getElementById('donation-form').style.display = 'block';
}

// Function to close the donation form
function closeDonationForm() {
    document.getElementById('donation-form').style.display = 'none';
}

