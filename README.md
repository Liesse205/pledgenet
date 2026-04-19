# PledgeNet
### Description
PledgeNet is a ledger-based donation transparency system that tracks donations, expenses, and audit logs to ensure full financial traceability for funding projects.
### Core Features
- Donation tracking per project
- Expense tracking with proof uploads
- Audit logs for every transaction
- User verification levels
- Risk scoring for suspicious activity
- Project funding dashboards
### Tech Stack
- Python, Flask, PostgreSQL, REST API
### Setup Instructions
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. psql -d pledgenet -f database/schema.sql
5. python run.py
