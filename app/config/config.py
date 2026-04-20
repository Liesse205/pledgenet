import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    # Use PostgreSQL if DATABASE_URL is provided, else fallback to SQLite for local runnability
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///pledgenet.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
