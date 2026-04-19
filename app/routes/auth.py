from flask import Blueprint, jsonify
from app.models.audit_log import AuditLog
from app.models.risk_score import RiskScore

audit_bp = Blueprint('audit', __name__)

@audit_bp.route('/audit-logs', methods=['GET'])
def get_audit_logs():
    logs = AuditLog.query.order_by(AuditLog.timestamp.desc()).all()
    return jsonify([{
        'id': log.id,
        'action_type': log.action_type,
        'entity_type': log.entity_type,
        'entity_id': log.entity_id,
        'details': log.details,
        'timestamp': log.timestamp.isoformat()
    } for log in logs]), 200

@audit_bp.route('/risk-logs', methods=['GET'])
def get_risk_logs():
    scores = RiskScore.query.order_by(RiskScore.timestamp.desc()).all()
    return jsonify([{
        'id': score.id,
        'user_id': score.user_id,
        'transaction_id': score.transaction_id,
        'score': float(score.score),
        'reason': score.reason,
        'timestamp': score.timestamp.isoformat()
    } for score in scores]), 200
