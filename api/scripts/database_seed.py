import sys
import os

# Adiciona o caminho absoluto à pasta `api/app` ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import User, Country, Team, Fighter, Fight, FightResult

app = create_app()

def add_default_user():
  with app.app_context():
      new_user = User(username="Caio Rosa", email="160173006@esg.ipsantarem.pt", role="ADMIN")
      new_user.set_password("123456")
      db.session.add(new_user)
      db.session.commit()
      print("✔ Default user added.")

def add_default_countries():
  with app.app_context():
      country_names = [
          "Portugal", "Brasil", "Espanha", "França", "Inglaterra", "Itália", "Argentina",
          "Uruguai", "Holanda", "Bélgica", "Suécia", "Dinamarca", "Noruega", "Finlândia",
          "Suíça", "Áustria", "Polônia", "República Checa", "Hungria", "Rússia", "Turquia",
          "Grécia", "Irlanda", "Escócia", "País de Gales", "Islândia", "Croácia", "Alemanha"
      ]
      countries = [Country(name=name) for name in country_names]
      db.session.add_all(countries)
      db.session.commit()
      print("✔ Countries added.")

def add_default_teams():
  with app.app_context():
      portugal = Country.query.filter_by(name="Portugal").first()
      brasil = Country.query.filter_by(name="Brasil").first()

      if not portugal or not brasil:
          print("Países Portugal ou Brasil não encontrados. Corre a função de países primeiro.")
          return

      teams = [
          Team(name="CT - Team", country_id=portugal.id, coach_name="Talisson Santos"),
          Team(name="Sport Lisboa e Benfica", country_id=portugal.id, coach_name="Roger Schmidt"),
          Team(name="Futebol Clube do Porto", country_id=portugal.id, coach_name="Sérgio Conceição"),
          Team(name="Sporting Clube de Portugal", country_id=portugal.id, coach_name="Rúben Amorim"),
          Team(name="Clube de Regatas do Flamengo", country_id=brasil.id, coach_name="Jorge Jesus"),
          Team(name="São Paulo Futebol Clube", country_id=brasil.id, coach_name="Dorival Júnior"),
          Team(name="Santos Futebol Clube", country_id=brasil.id, coach_name="Fábio Carille"),
      ]
      db.session.add_all(teams)
      db.session.commit()
      print("✔ Teams added.")

def add_default_fighters():
  with app.app_context():
      teams = Team.query.all()
      if not teams:
          print("Nenhuma equipa encontrada. Corre a função de equipas primeiro.")
          return

      fighters = [
          {"first_name": "Ricado", "last_name": "silva", "nickname": "the wall", "weight": "53.5", "team_id": teams[0].id, "wins": 0, "losses":  0, "draws": 0},
          {"first_name": "andre", "last_name": "moreira", "nickname": "kong", "weight": "53.5", "team_id": teams[1].id, "wins": 0, "losses":  0, "draws": 0},
          
      ]

      for fighter in fighters:
          new_fighter = Fighter(
              first_name=fighter["first_name"],
              last_name=fighter["last_name"],
              nickname=fighter["nickname"],
              weight=fighter["weight"],
              team_id=fighter["team_id"],
              wins=fighter["wins"],
              losses=fighter["losses"],
              draws=fighter["draws"]
          )
          db.session.add(new_fighter)

      db.session.commit()
      print("✔ Fighters added.")

def clear_database():
  with app.app_context():
      db.drop_all()
      db.create_all()
      print("✔ Database cleared and recreated.")

if __name__ == "__main__":
  clear_database()
  add_default_user()
  add_default_countries()
  add_default_teams()
  add_default_fighters()
  print("Database seeded com sucesso.")
