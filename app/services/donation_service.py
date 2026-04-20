from app.models.donation import Donation
from app.models.project import Project
from app.services.audit_service import AuditService
from app.services.risk_service import RiskService
from app.services.verification_service import VerificationService
from app import db

class DonationService:
    @staticmethod
    def record_donation(user_id, project_id, amount):
        # Verification check
        can_donate, error = VerificationService.can_donate(user_id, amount)
        if not can_donate:
            return None, error

        project = Project.query.get(project_id)
        if not project:
            return None, "Project not found"
        
        # Automatic balance update
        donation = Donation(user_id=user_id, project_id=project_id, amount=amount)
        project.current_amount += amount
        
        db.session.add(donation)
        db.session.flush() # Get donation ID
        
        # Risk scoring
        risk_score = RiskService.calculate_risk(user_id, donation.id, amount)
        donation.risk_score = risk_score
        
        db.session.commit()
        
        # Audit logging
        AuditService.log_action(
            "DONATION_CREATED", 
            "Donation", 
            donation.id, 
            {"user_id": user_id, "project_id": project_id, "amount": float(amount)}
        )
        
        return donation, None
