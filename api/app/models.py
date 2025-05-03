from . import db
from werkzeug.security import generate_password_hash, check_password_hash


# Define the User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)
    role = db.Column(db.Enum('ADMIN', 'USER'), default='user', nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp()) 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

   
# Define the Country model
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    
# Define the Team model
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    coach_name = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    country = db.relationship('Country', backref=db.backref('teams', lazy=True))


class Fighter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    nickname = db.Column(db.String(150), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    draws = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    team = db.relationship('Team', backref=db.backref('fighters', lazy=True))
    
class Fight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fighter_a_id = db.Column(db.Integer, db.ForeignKey('fighter.id'), nullable=False)
    fighter_b_id = db.Column(db.Integer, db.ForeignKey('fighter.id'), nullable=False)
    schedule_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(150), nullable=False)
    rounds = db.Column(db.Integer, nullable=False)
    rounds_minutes = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    fighter_a = db.relationship('Fighter', foreign_keys=[fighter_a_id], backref=db.backref('fights_as_fighter_a', lazy=True))
    fighter_b = db.relationship('Fighter', foreign_keys=[fighter_b_id], backref=db.backref('fights_as_fighter_b', lazy=True))
    
class FightResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fight_id = db.Column(db.Integer, db.ForeignKey('fight.id'), nullable=False)
    winner_id = db.Column(db.Integer, db.ForeignKey('fighter.id'), nullable=False)
    method = db.Column(db.String(50), nullable=False)  # e.g., KO, Submission, Decision
    round_number = db.Column(db.Integer, nullable=False)
    time = db.Column(db.String(10), nullable=False)  # e.g., "3:45"
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    fight = db.relationship('Fight', backref=db.backref('results', lazy=True))
    winner = db.relationship('Fighter', foreign_keys=[winner_id], backref=db.backref('wins', lazy=True))