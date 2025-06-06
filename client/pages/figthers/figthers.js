
import { FighterService } from "../../js/services/fighterService.js";
import { FighterSimplePostCard } from "../../js/components/figtherSimplePostCard.js";

const baseUrl = 'http://127.0.0.1:5000';


function buildFighterCard(fighter) {
  const fullName = fighter.first_name + ' ' + fighter.last_name;

  const imageRandomNumber = Math.floor(Math.random() * 16) + 1;
  const imagePath = `../../assets/imagens/figthers/${imageRandomNumber}.png`;

  return new FighterSimplePostCard({
    id: fighter.id,
    fullName: fullName.toLocaleUpperCase(),
    country: fighter.country,
    imgSrc: imagePath
  }).render();
}

function appendFighterCard(container, card) {
  container.appendChild(card);
}

function buildFighterCardList(fighters) {
  const container = document.getElementById('fighter-cards-container');

  fighters.forEach(fighter => {
    const card = buildFighterCard(fighter);

    appendFighterCard(container, card);
  });
}


/**
 * Abre um dxPopup com os detalhes de um lutador
 * @param {number} fighterId - O ID do lutador a mostrar
 * @returns {void}
 */
async function openAthleteDetails(fighterId) {
  console.log("Abrindo detalhes do lutador:", fighterId);
  const fighterService = new FighterService(baseUrl);

  try {
    const {data: fighter} = await fighterService.getByIdAsync(fighterId);

    if (!fighter) {
      DevExpress.ui.notify('Lutador não encontrado.', 'error', 3000);
      return;
    }

    const fullName = `${fighter.first_name} ${fighter.last_name}`.toUpperCase();
    const imageRandomNumber = Math.floor(Math.random() * 16) + 1;
    const imagePath = `../../assets/imagens/figthers/${imageRandomNumber}.png`;

    const card = new FighterSimplePostCard({
      id: fighter.id,
      fullName,
      country: fighter.country?.name || 'N/A',
      imgSrc: imagePath
    }).render();

    let popupElement = $("#fighter-details-popup");
    let popupInstance = DevExpress.ui.dxPopup.getInstance(popupElement[0]);

    $("#fighter-details-popup").dxPopup({
        title: `Detalhes do Atleta`,
        contentTemplate: () => {
          const container = document.createElement('div');
          container.className = "fighter-popup-container";

          // Lado esquerdo: Imagem
          const left = document.createElement('div');
          left.className = "fighter-popup-left";
          left.innerHTML = `<img src="${imagePath}" alt="${fighter.nickname}">`;

          // Nome completo e equipa
          const fullName = `${fighter.first_name} ${fighter.last_name}`;
          const teamName = fighter.team?.name || 'Equipa desconhecida';
          const countryName = fighter.team?.country?.name || 'País desconhecido';

          // Lado direito: Dados do atleta
          const right = document.createElement('div');
          right.className = "fighter-popup-right";
          right.innerHTML = `
    <h2>"${fighter.nickname}" ${fullName}</h2>
    <small class="text-muted">Atleta profissional de MMA</small>

    <div class="fighter-popup-meta">
      <div><strong>Peso:</strong> ${fighter.weight} KG</div>
      <div><strong>Vitórias:</strong> ${fighter.wins}</div>
      <div><strong>Derrotas:</strong> ${fighter.losses}</div>
      <div><strong>Empates:</strong> ${fighter.draws}</div>
      <div><strong>País:</strong> ${countryName}</div>
      <div><strong>Equipa:</strong> ${teamName}</div>
      <div><strong>Status:</strong> ${fighter.active ? "Ativo" : "Inativo"}</div>
    </div>
  `;

          container.appendChild(left);
          container.appendChild(right);

          // Bio fictícia
          const bio = document.createElement('div');
          bio.className = "fighter-popup-bio";
          bio.innerHTML = `
    <h3>Sobre "${fighter.nickname}"</h3>
    <p>
      ${fighter.first_name} é um atleta da equipa ${teamName}, representando orgulhosamente ${countryName}.
      Com ${fighter.wins} vitórias e ${fighter.losses} derrotas na sua carreira, destaca-se pela sua dedicação e espírito competitivo.
      O seu estilo de luta combina técnica e resistência, tornando-o um adversário formidável no ringue.
    </p>
  `;

          const wrapper = document.createElement('div');
          wrapper.appendChild(container);
          wrapper.appendChild(bio);

          return wrapper;
        },
        showCloseButton: true,
        showTitle: true,
        width: '80vw',
        height: 'auto',
        visible: true,
        dragEnabled: false,
        closeOnOutsideClick: false,
        position: {
          of: window,
          my: 'center center',
          at: 'center center'
        }
      });
  } catch (error) {
    console.error("Erro ao carregar detalhes do lutador:", error);
    DevExpress.ui.notify("Erro ao carregar dados do lutador.", "error", 3000);
  }
}

//add this function to the window object to be accessible globally
window.openAthleteDetails = openAthleteDetails;

document.addEventListener('DOMContentLoaded', async () => {

  const fighterService = new FighterService(baseUrl);
  const { data: fighters } = await fighterService.getAsync();

  buildFighterCardList(fighters);


})