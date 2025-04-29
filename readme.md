# Projeto: Sistema Web para Evento de Luta

**Descrição do Projecto**  
Desenvolver uma aplicação web completa para gestão e apresentação de um evento de luta. O sistema permitirá o registo e a visualização de lutadores, equipas e combates, além de gerar classificações dinâmicas com base nos resultados. Haverá perfis detalhados de atletas, informação sobre cada combate, formulário de inscrição/contacto e um design responsivo para dispositivos móveis e desktop. A aplicação terá um back-end em Python/Flask com API REST e uma base de dados relacional, e um front-end em HTML, CSS e JavaScript, garantindo uma experiência interactiva e moderna para administradores, participantes e público.

---

## 1. Brainstorming de Funcionalidades

| Área          | Funcionalidade                             | Descrição                                                                  |
|---------------|--------------------------------------------|----------------------------------------------------------------------------|
| **Front-end** | Página inicial                             | Banner do evento, menu de navegação para “Lutadores”, “Combates”, “Classificações” |
|               | Perfil de lutador                          | Foto, nome, categoria, equipa, estatísticas (v–d–e), biografia            |
|               | Lista de combates                          | Cartaz do evento: data, hora, local, lutador A vs lutador B               |
|               | Tabela de classificações                   | Classificação por categoria (peso), por vitórias, por equipa              |
|               | Formulário de contacto/inscrição           | Inscrição de atletas ou contacto de patrocinadores                        |
| **Back-end**  | API REST com Flask                         | Endpoints para CRUD de lutadores, combates, equipas, classificações       |
|               | Autenticação e Autorização                 | Implementar login/logout e controlo de permissões (admin vs visitante)    |
|               | Base de dados                              | Modelo: Lutador, Equipa, Combate, Resultado                                |
|               | Lógica de cálculo de classificação         | Script Python que actualiza classificação após cada combate               |
| **UX/UI**     | Design responsivo                          | Mobile & desktop. CSS (Flex/Grid) + media queries                         |
|               | Tema visual                                | Cores alusivas ao combate (preto/vermelho), tipografia forte               |
| **Extras**    | Estatísticas em tempo real (opcional)      | WebSocket para actualizações de resultados “live”                         |

---

## 2. Blueprint / Guia Inicial

### 2.1. Arquitectura Geral  

![modelo](./image-1.png)

1. **Front-end**  
   - HTML semântico + CSS (Flexbox/Grid) + JavaScript (fetch/Axios).  
   - Framework leve (opcional): Bootstrap ou Tailwind para agilizar.  

2. **Back-end (Flask)**  
   - Estrutura de pastas:  
     ```  
     /app  
       /static  
       /templates  
       models.py  
       routes.py  
       rankings.py  
       auth.py  
       __init__.py  
     config.py  
     run.py  
     ```  
   - **models.py**: definições SQLAlchemy  
   - **routes.py**: endpoints REST  
   - **auth.py**: login, logout, decorator de permissões  
   - **rankings.py**: lógica de negócio  

3. **Base de Dados**  
   - Tabelas principais:  
     - **Lutador** (id, nome, peso, equipa_id, vitorias, derrotas, empates, foto)  
     - **Equipa** (id, nome, país)  
     - **Combate** (id, lutadorA_id, lutadorB_id, data, resultado_id)  
     - **Resultado** (id, combate_id, vencedor_id, método)  

---

### 2.2. Ações Utilizadores


| #  | Como…                | Quero…                                            | Para…                              |
|----|----------------------|---------------------------------------------------|------------------------------------|
| 1  | visitante            | ver a lista de combates                           | saber quem luta e quando           |
| 2  | administrador        | criar/editar perfis de lutadores                  | manter dados actualizados          |
| 3  | visitante            | consultar classificação por categoria de peso     | identificar os melhores lutadores  |
| 4  | administrador        | registar resultados de um combate                 | actualizar automaticamente a classificação |
---



## 3. Cronograma e Micro-tarefas (2 semanas)

| Semana | Dias  | Entrega / Tarefa                                                                                 |
|--------|-------|--------------------------------------------------------------------------------------------------|
| 1      | 1     | Kick-off: definir requisitos, instalar dependências, configurar repositório Git                   |
|        | 2     | Modelação BD: criar diagrama ER, definir migrations                                              |
|        | 3     | Wireframes: desenhar páginas principais (Home, Lutadores, Combates, Perfil)                      |
|        | 4     | CRUD Lutador/Equipa: implementar models, migrations, endpoints básicos                           |
|        | 5     | Front-end Lutador: template lista e perfil, integração com API                                   |
|        | 6-7   | CRUD Combate: models, endpoints, formulários de agendamento e listagem                           |
| 2      | 8     | Lançamento de Resultados: form, endpoint e lógica de ranking                                     |
|        | 9     | Autenticação: login/logout, restrição de rotas admin                                            |
|        | 10    | Design responsivo: aplicar media queries, testar mobile                                         |
|        | 11    | Testes funcionais: elaborar cenários, registar bugs                                               |
|        | 12    | Documentação: README, manual de utilizador                                            |
|        | 13    | Deploy: configurar github pages                               |
|        | 14    | Apresentação final: preparar slides, demo ao vivo                                               |

---

## 4. Tarefas

- Front-end (HTML/CSS/Javascript)
  - Desenhar wireframes com proposta dos layouts para cada pagina
  - Criar css base do projeto (definir cores, tipografia)
  - Criar estrutura html base
  - Criar layout das paginas definidos na wireframe
  - criar componentes html (cards, modals, tabelas)
  - Criar javascript para interagir com as paginas e validar formularios 
  - Implementar ZOD para validação de dados
  - Implementar sistema de login para admins
  - Implementar axios para chamadas a API
  - Criar mockup dos dados para testar API
  - Documentar e corrigir bugs
  - Testes end to end

- Base de dados
  - Criar modelo ER
  - Criar sql
  - Popular tabelas com dados

- Back-end (Flask Models/API) 
  - Definir modelos
  - Criar migrations
  - Implementar CRUD Lutador
  - Implementar CRUD Equipa
  - Implementar CRUD Combate
  - Implementar CRUD Resultado
  - Implementar rotas de autenticação
  - Implementar regras de negocio 

- QA & Documentação da API
  - Escrever casos de teste e realizar testes manuais
  - Documentar API (Swagger)
  - Criar manual do utilizador (admin) e instruções para fazer deeploy


<!-- 


---

## 5. Próximos Passos Imediatos

1. **Kick-off**: validar blueprint e ajustar user stories.  
2. **Setup**: repositório GitHub, branches (main, develop, feature/*).  
3. **Ambiente**: configurar virtualenv, instalar Flask, SQLAlchemy, Alembic.  
4. **Comunicação**: criar canal Slack/Discord e definir horário dos stand-ups.  
5. **Issue Tracking**: criar issues no GitHub conforme micro-tarefas acima.   -->
