# Fighter Flow - Projeto Base

Este projeto é o ponto de partida para a equipa de frontend do Fighter Flow. A estrutura foi desenhada para ser simples, acessível e fácil de manter por membros iniciantes.

## Estrutura

```
fighter-flow/
│
├── index.html              # Página principal
├── login.html              # Página de login
├── atletas.html            # (a desenvolver)
├── evento.html             # (a desenvolver)
├── dashboard.html          # (a desenvolver - rota privada)
│
├── /css
│   ├── global.css          # Estilos globais e cores
│   └── pages/              # Estilos específicos por página
│
├── /js
│   ├── main.js             # Lógica comum (menu, etc.)
│   ├── auth.js             # Login
│   └── pages/              # Scripts por página
│
├── /assets                 # Imagens e fontes
│   ├── /img
│   └── /fonts
│
└── /api                    # Lógica de ligação ao backend (futura)
```

## Como começar

1. Abrir a pasta no VSCode.
2. Instalar a extensão **Live Server** para ver as páginas localmente.
3. Abrir `index.html` e clicar em "Go Live".
4. Cada membro trabalha no ficheiro da sua página.
5. Sofia edita `global.css` com as cores, tipos de letra e estilos globais.

## Backend

O backend já está disponível e funcional em `http://localhost:5000`. O login utiliza um endpoint POST em `/api/login`.


