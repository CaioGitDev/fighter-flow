### Instalar o git
* https://git-scm.com/downloads/win

## verificar instalação do git
* git -v

## clonar repositorio
* git clone https://github.com/CaioGitDev/fighter-flow.git

## enter na pasta
* cd .\fighter-flow\

## abrir visual studio
* code .

### instalar dependencias
* pip install -r requirements.txt


### correr scripts de inicialização da base de dados
* python scripts/database_seed.py

### executar api em modo debug
* python run.py

### ativar ambiente virtual para correr flask
* .\venv\Scripts\Activate

Comando	Função
flask db init	              Inicializa o diretório de migrations (apenas 1x no início do projeto) - SO EXECUTAR UMA UNICA VEZ
flask db migrate -m "..."	  Gera o script com base nas alterações feitas nos modelos (models.py)
flask db upgrade	          Aplica o script (as alterações) à base de dados



# Ativar o ambiente virtual (altera conforme o teu SO ou ambiente)
source venv/bin/activate  # Linux/macOS
# .\venv\Scripts\activate  # Windows

# Atualiza o pip, setuptools e wheel
pip install --upgrade pip setuptools wheel

# Reinstala tudo a partir do ficheiro atualizado
pip install -r requirements.txt
