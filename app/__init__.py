from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.projects import projects_bp
    from app.routes.donations import donations_bp
    from app.routes.expenses import expenses_bp
    from app.routes.audit import audit_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(projects_bp, url_prefix='/projects')
    app.register_blueprint(donations_bp, url_prefix='/donations')
    app.register_blueprint(expenses_bp, url_prefix='/expenses')
    app.register_blueprint(audit_bp, url_prefix='/audit')

    return app
