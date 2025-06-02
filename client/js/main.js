import { LoginService } from './services/login.js';

const baseUrl = 'http://127.0.0.1:5000';
const loginService = new LoginService(baseUrl);

function addDynamicLinks() {
  const loginLink = document.getElementById('login-link');
  const logoutLink = document.getElementById('logout-link');

  if (loginService.isLoggedIn()) {
    loginLink.style.display = 'none';
    logoutLink.style.display = 'block';
    logoutLink.addEventListener('click', () => {
      loginService.logout();
    });
  } else {
    loginLink.style.display = 'block';
    logoutLink.style.display = 'none';
  }
}

document.addEventListener('DOMContentLoaded', async () => {

  addDynamicLinks();

});