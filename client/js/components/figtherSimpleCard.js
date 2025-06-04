export class FighterSimpleCard {
  /**
   * Cria uma nova instância de FighterSimpleCard
   * @param {string} name - Nome do atleta
   * @param {string} imgSrc - Caminho da imagem
   */
  constructor(name, imgSrc) {
    this.name = name;
    this.imgSrc = imgSrc;
  }

 
  render() {
    // Container principal
    const card = document.createElement("div");
    card.className = "simple-post-card is-term is-image-zoom-area";

    // Link da imagem
    const imageLink = document.createElement("a");
    imageLink.className = "image ratio ratio-16x9 is-image-zoom";
    imageLink.href = "#";
    imageLink.title = this.name;

    // Imagem
    const img = document.createElement("img");
    img.width = 600;
    img.height = 400;
    img.src = this.imgSrc;
    img.alt = `${this.name}`;
    img.className = "attachment-medium size-medium";
    img.sizes = "400px";
    img.decoding = "async";

    imageLink.appendChild(img);

    // Conteúdo
    const content = document.createElement("div");
    content.className = "content";

    const titleLink = document.createElement("a");
    titleLink.className = "title";
    titleLink.href = "#";
    titleLink.title = this.name;

    const title = document.createElement("h3");
    title.textContent = this.name;

    titleLink.appendChild(title);
    content.appendChild(titleLink);

    // Montar o card
    card.appendChild(imageLink);
    card.appendChild(content);

    return card;
  }
}
