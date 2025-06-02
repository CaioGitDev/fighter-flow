import { LoginService } from '../../js/services/login.js';

document.addEventListener('DOMContentLoaded', async () => {

  const baseUrl = 'http://127.0.0.1:5000';

  const loginForm = document.getElementById('login-form');
  const errorMessage = document.getElementById('error-message');

  loginForm.addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent the default form submission

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const loginService = new LoginService(baseUrl);
    
    // Validate email and password
    if (!loginService.validateEmail(email)) {
      errorMessage.textContent = 'Please enter a valid email address.';
      errorMessage.style.display = 'block';
      setTimeout(() => {
        errorMessage.style.display = 'none';
      }, 5000); // Hide the error message after 5 seconds
      return;
    }

    const result = await loginService.loginAsync(email, password);
    if (result) {
      console.log('Login successful');
      // Redirect to the main page or perform other actions
      window.location.href = '../../index.html';
    } else {
      // Show an error message to the user
      errorMessage.textContent = 'Invalid email or password. Please try again.';
      errorMessage.style.display = 'block';
      setTimeout(() => {
        errorMessage.style.display = 'none';
      }, 5000); // Hide the error message after 3 seconds
    }
  });

});
