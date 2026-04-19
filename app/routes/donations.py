from flask import Blueprint, request, jsonify
from app.services.ledger_service import LedgerService
from app.models.donation import Donation

donations_bp = Blueprint('donations', __name__)

@donations_bp.route('', methods=['POST'])
def create_donation():
    data = request.get_json()
    user_id = data.get('user_id')
    project_id = data.get('project_id')
    amount = data.get('amount')
    
    if not user_id or not project_id or not amount:
        return jsonify({'error': 'Missing required fields'}), 400
    
    donation, error = LedgerService.record_donation(user_id, project_id, amount)
    if error:
        return jsonify({'error': error}), 400
    
    return jsonify(donation.to_dict()), 201

@donations_bp.route('/project/<int:project_id>', methods=['GET'])
def get_project_donations(project_id):
    donations = Donation.query.filter_by(project_id=project_id).all()
    return jsonify([d.to_dict() for d in donations]), 200
