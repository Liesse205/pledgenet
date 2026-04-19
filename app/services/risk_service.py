from app.models.risk_score import RiskScore
from app import db

class RiskService:
    @staticmethod
    def calculate_risk(user_id, transaction_id, amount):
        # Simplified risk scoring for MVP
        score = 0.0
        reason = "Normal transaction"
        
        if amount > 10000:
            score = 8.5
            reason = "High amount threshold exceeded"
        elif amount > 1000:
            score = 3.0
            reason = "Moderate amount"
            
        risk = RiskScore(
            user_id=user_id,
            transaction_id=transaction_id,
            score=score,
            reason=reason
        )
        db.session.add(risk)
        db.session.commit()
        return score
