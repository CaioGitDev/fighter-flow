export class FighterSimplePostCard {
  /**
   * Cria uma nova instância de FighterSimplePostCard
   * @param {Object} fighter - Dados do atleta
   * @param {number|string} fighter.id - ID do atleta
   * @param {string} fighter.fullName - Nome completo do atleta
   * @param {string} fighter.country - País do atleta
   * @param {string} fighter.imgSrc - Caminho da imagem
   */
  constructor({ id, fullName, country, imgSrc }) {
    this.id = id;
    this.fullName = fullName;
    this.country = country;
    this.imgSrc = imgSrc;
  }

  /**
   * Gera o elemento HTML completo da ficha do atleta
   * @returns {HTMLElement} - O elemento `.simple-post-card`
   */
  render() {
    // Container principal
    const card = document.createElement("div");
    card.className = "simple-post-card is-athlete";

    // Link da imagem
    const imageLink = document.createElement("a");
    imageLink.className = "image ratio ratio-1x1 is-image-zoom";

    const img = document.createElement("img");
    img.width = 500;
    img.height = 345;
    img.src = this.imgSrc;
    img.alt = `${this.fullName} Avatar 500x345`;
    img.className = "attachment-medium size-medium";
    img.sizes = "320px";
    img.decoding = "async";
    img.onclick = async () => await window.openAthleteDetails(this.id);

    imageLink.appendChild(img);

    // Conteúdo textual
    const content = document.createElement("div");
    content.className = "content";

    const titleLink = document.createElement("a");
    titleLink.className = "title text-center";
    titleLink.onclick = async() => await window.openAthleteDetails(this.id);

    const title = document.createElement("h3");
    title.textContent = this.fullName;

    titleLink.appendChild(title);

    const countryDiv = document.createElement("div");
    countryDiv.className = "country";
    countryDiv.textContent = this.country;

    content.appendChild(titleLink);
    content.appendChild(countryDiv);

    // Montar o card
    card.appendChild(imageLink);
    card.appendChild(content);

    return card;
  }
}
