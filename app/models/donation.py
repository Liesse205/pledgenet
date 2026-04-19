from app import db
from datetime import datetime

class Donation(db.Model):
    __tablename__ = 'donations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    amount = db.Column(db.Numeric(15, 2), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    risk_score = db.Column(db.Numeric(5, 2), default=0.00)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'project_id': self.project_id,
            'amount': float(self.amount),
            'timestamp': self.timestamp.isoformat(),
            'risk_score': float(self.risk_score)
        }
