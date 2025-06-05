// js/router.js

const Router = (() => {
  const BASE_PATH = window.location.origin
    .replace(/\/(pages|figthers|login|gestao)[^\/]*/i, '') // Remove subpasta
    .replace(/\/$/, ''); // Remove trailing slash
console.log('Base Path:', BASE_PATH);
  const routes = {
    home: `${BASE_PATH}/client/index.html`,
    eventos: `${BASE_PATH}/client/pages/eventos/index.html`,
    atletas: `${BASE_PATH}/client/pages/figthers/index.html`,
    gestao: `${BASE_PATH}/client/pages/gestao/index.html`,
    login: `${BASE_PATH}/client/pages/login/index.html`,
  };

  const setNavLinks = () => {
    const navMap = {
      '#link-eventos': routes.eventos,
      '#link-atletas': routes.atletas,
      '#link-gestao': routes.gestao,
      '#link-login': routes.login,
      '#logout-link': routes.home // ou uma rota de logout
    };

    for (const [selector, url] of Object.entries(navMap)) {
      const el = document.querySelector(selector);
      if (el) el.setAttribute('href', url);
    }
  };

  return {
    init: () => setNavLinks(),
    routes
  };
})();

// Inicializa o sistema de rotas após o carregamento da página
window.addEventListener("DOMContentLoaded", () => {
  Router.init();
});
