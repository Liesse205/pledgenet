from app.models.expense import Expense
from app.models.project import Project
from app.services.audit_service import AuditService
from app import db

class ExpenseService:
    @staticmethod
    def record_expense(project_id, amount, category, description, proof_url):
        project = Project.query.get(project_id)
        if not project:
            return None, "Project not found"
        
        if project.current_amount < amount:
            return None, "Insufficient funds in project balance"
        
        # Deduct from project balance
        expense = Expense(
            project_id=project_id, 
            amount=amount, 
            category=category, 
            description=description, 
            proof_url=proof_url
        )
        project.current_amount -= amount
        
        db.session.add(expense)
        db.session.commit()
        
        # Audit logging
        AuditService.log_action(
            "EXPENSE_CREATED", 
            "Expense", 
            expense.id, 
            {"project_id": project_id, "amount": float(amount), "category": category}
        )
        
        return expense, None
