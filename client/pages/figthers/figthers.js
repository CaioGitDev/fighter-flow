
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

document.addEventListener('DOMContentLoaded', async () => {

  const fighterService = new FighterService(baseUrl);
  const { data: fighters } = await fighterService.getFightersAsync();

  buildFighterCardList(fighters);


})