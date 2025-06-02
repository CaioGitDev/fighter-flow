import { LoginService } from './services/login.js';

const baseUrl = 'http://127.0.0.1:5000';

document.addEventListener('DOMContentLoaded', async () => {

  const user = {
    "email": "160173006@esg.ipsantarem.pt",
    "password": "123456"
  }

  const loginService = new LoginService(baseUrl);

  const result = await loginService.loginAsync(user.email, user.password)
  if (result) {
    console.log('Login successful');
    // Redirect to the main page or perform other actions
    //window.location.href = 'main.html';
  } else {
    console.error('Login failed');
    // Show an error message to the user
  }
});