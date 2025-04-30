import sys
import os

# Adiciona o caminho absoluto à pasta `api/app` ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
  new_user = User(username="Caio Rosa", email="160173006@esg.ipsantarem.pt")
  new_user.set_password("123456")
  db.session.add(new_user)
  db.session.commit()
  print("Database seeded with initial data.")