from app.models.project import Project
from app import db

class ProjectService:
    @staticmethod
    def create_project(title, description, goal_amount, owner_id):
        project = Project(
            title=title, 
            description=description, 
            goal_amount=goal_amount, 
            owner_id=owner_id
        )
        db.session.add(project)
        db.session.commit()
        return project

    @staticmethod
    def get_all_projects():
        return Project.query.all()

    @staticmethod
    def get_project_by_id(project_id):
        return Project.query.get(project_id)
