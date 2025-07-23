// This code runs after the page loads
document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('contactForm');

  form.addEventListener('submit', function (event) {
    // Grab values from the form fields
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Basic validation rules
    if (name === '' || email === '' || message === '') {
      alert('Please fill in all fields.');
      event.preventDefault(); // Stops the form from submitting
      return;
    }

    if (!email.includes('@') || !email.includes('.')) {
      alert('Please enter a valid email address.');
      event.preventDefault();
      return;
    }

    if (message.length < 10) {
      alert('Your message should be at least 10 characters long.');
      event.preventDefault();
      return;
    }

    // If all is good, form will be submitted to backend
  });
});
