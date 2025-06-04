import { LoginService } from './services/login.js';
import { FighterService } from './services/fighterService.js';
import { FighterSimpleCard } from './components/figtherSimpleCard.js';

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

async function buildFighterCards() {
  const fighterService = new FighterService(baseUrl);
  const { data: fighters } = await fighterService.getFightersAsync();

  const container = document.getElementById('fighter-cards-container');

  console.log('Fighters fetched:', fighters);

  fighters.forEach(fighter => {
    const fullName = fighter.first_name + ' ' + fighter.last_name;

    const card = new FighterSimpleCard(fullName.toLocaleUpperCase(), "assets/imagens/1.jpg").render();
    container.appendChild(card);
  });
}

document.addEventListener('DOMContentLoaded', async () => {
  addDynamicLinks();
  buildFighterCards();
});