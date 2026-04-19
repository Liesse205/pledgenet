from app import db
from datetime import datetime

class RiskScore(db.Model):
    __tablename__ = 'risk_scores'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    transaction_id = db.Column(db.Integer)
    score = db.Column(db.Numeric(5, 2), nullable=False)
    reason = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'transaction_id': self.transaction_id,
            'score': float(self.score),
            'reason': self.reason,
            'timestamp': self.timestamp.isoformat()
        }
