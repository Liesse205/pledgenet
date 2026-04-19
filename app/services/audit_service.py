from app.models.audit_log import AuditLog
from app import db

class AuditService:
    @staticmethod
    def log_action(action_type, entity_type, entity_id, details):
        log = AuditLog(
            action_type=action_type,
            entity_type=entity_type,
            entity_id=entity_id,
            details=details
        )
        db.session.add(log)
        db.session.commit()
