from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app import db

class AuthService:
    @staticmethod
    def register_user(name, email, password):
        if User.query.filter_by(email=email).first():
            return None, "Email already exists"
        
        hashed_password = generate_password_hash(password)
        user = User(name=name, email=email, password_hash=hashed_password)
        
        db.session.add(user)
        db.session.commit()
        return user, None

    @staticmethod
    def login_user(email, password):
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            return None, "Invalid email or password"
        
        # Simplified token for MVP (in real app use JWT)
        return f"fake-jwt-token-for-user-{user.id}", None
