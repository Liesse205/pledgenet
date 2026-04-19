from app import db
from datetime import datetime

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    amount = db.Column(db.Numeric(15, 2), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    proof_url = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'amount': float(self.amount),
            'category': self.category,
            'description': self.description,
            'proof_url': self.proof_url,
            'timestamp': self.timestamp.isoformat()
        }
