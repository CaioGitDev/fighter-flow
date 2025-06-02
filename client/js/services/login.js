export class LoginService {
  constructor(baseUrl) {
    this.baseUrl = baseUrl;
  }

  async loginAsync(email, password) {
    try {
      const response = await fetch(`${this.baseUrl}/api/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });

      if (!response.ok) {
        throw new Error('Login failed');
      }

      const data = await response.json();
      if (data.access_token) {
        localStorage.setItem('token', data.access_token);
        return true;
      } else {
        return false;
      }
    } catch (error) {
      console.log('Error during login:', error);
      return false;
    }

  }

  isLoggedIn() {
    const token = localStorage.getItem('token');
    return token !== null && token !== '';
  }

  logout() {
    localStorage.removeItem('token');
    window.location.href = './pages/login/index.html'; // Redirect to login page
  }

  validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
  validatePassword(password) {
    // Example validation: at least 8 characters, one uppercase, one lowercase, one number
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/;
    return passwordRegex.test(password);
  }
}