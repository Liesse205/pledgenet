from flask import Blueprint, request, jsonify
from app.services.ledger_service import LedgerService
from app.models.expense import Expense

expenses_bp = Blueprint('expenses', __name__)

@expenses_bp.route('', methods=['POST'])
def create_expense():
    data = request.get_json()
    project_id = data.get('project_id')
    amount = data.get('amount')
    category = data.get('category')
    description = data.get('description')
    proof_url = data.get('proof_url')
    
    if not project_id or not amount or not category:
        return jsonify({'error': 'Missing required fields'}), 400
    
    expense, error = LedgerService.record_expense(project_id, amount, category, description, proof_url)
    if error:
        return jsonify({'error': error}), 400
    
    return jsonify(expense.to_dict()), 201

@expenses_bp.route('/project/<int:project_id>', methods=['GET'])
def get_project_expenses(project_id):
    expenses = Expense.query.filter_by(project_id=project_id).all()
    return jsonify([e.to_dict() for e in expenses]), 200
