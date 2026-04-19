from app import db
from datetime import datetime

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    goal_amount = db.Column(db.Numeric(15, 2), nullable=False)
    current_amount = db.Column(db.Numeric(15, 2), default=0.00)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    donations = db.relationship('Donation', backref='project', lazy=True)
    expenses = db.relationship('Expense', backref='project', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'goal_amount': float(self.goal_amount),
            'current_amount': float(self.current_amount),
            'owner_id': self.owner_id,
            'created_at': self.created_at.isoformat()
        }
