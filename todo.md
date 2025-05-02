
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
