import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  SECRET_KEY = os.getenv('SECRET_KEY')
  JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
  JWT_ACCESS_TOKEN_EXPIRES_IN = os.getenv('JWT_ACCESS_TOKEN_EXPIRES')
  SQLALCHEMY_DATABASE_URI = (
        f"mysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
        f"@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False 