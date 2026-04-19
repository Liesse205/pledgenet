from flask import Blueprint, request, jsonify
from app.services.project_service import ProjectService

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('', methods=['GET'])
def get_projects():
    projects = ProjectService.get_all_projects()
    return jsonify([p.to_dict() for p in projects]), 200

@projects_bp.route('', methods=['POST'])
def create_project():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    goal_amount = data.get('goal_amount')
    owner_id = data.get('owner_id')
    
    if not title or not goal_amount or not owner_id:
        return jsonify({'error': 'Missing required fields'}), 400
    
    project = ProjectService.create_project(title, description, goal_amount, owner_id)
    return jsonify(project.to_dict()), 201

@projects_bp.route('/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = ProjectService.get_project_by_id(project_id)
    if not project:
        return jsonify({'error': 'Project not found'}), 404
    return jsonify(project.to_dict()), 200
