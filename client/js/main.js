import { LoginService } from './services/login.js';
import { FighterService } from './services/fighterService.js';
import { FighterSimpleCard } from './components/figtherSimpleCard.js';

const baseUrl = 'http://127.0.0.1:5000';
const loginService = new LoginService(baseUrl);

function addDynamicLinks() {
  const loginLink = document.getElementById('link-login');
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
  const { data: fighters } = await fighterService.getAsync();

  const container = document.getElementById('fighter-cards-container');

  const maxFighters = 4;
  const imagePathTemplate = 'assets/imagens/f{number}.jpg';
  fighters.forEach(fighter => {
    const fullName = fighter.first_name + ' ' + fighter.last_name;

    if (container.children.length >= maxFighters) {
      return; // Limita a 4 cards
    }

    const imageRandomNumber = Math.floor(Math.random() * 4) + 1; // Gera um número aleatório entre 1 e 4
    const imagePath = imagePathTemplate.replace('{number}', imageRandomNumber);

    const card = new FighterSimpleCard(fullName.toLocaleUpperCase(), imagePath).render();
    container.appendChild(card);
  });
}

function scrollToTop() {
  const scrollToTopElem = document.querySelector('#site-footer .scroll-to-top');
  if (scrollToTopElem) {
    scrollToTopElem.addEventListener('click', () => {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    });
  }
}

document.addEventListener('DOMContentLoaded', async () => {
  addDynamicLinks();
  buildFighterCards();
  scrollToTop();
});