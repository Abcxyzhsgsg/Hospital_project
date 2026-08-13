Hospital Appointment Management API

Simple FastAPI application managing patients, doctors, and appointments.

Features:
- FastAPI + Pydantic + SQLAlchemy
- Alembic migrations
- Prevents overlapping appointments per doctor
- Pytest tests with coverage
- GitHub Actions for linting, tests (coverage >=85%), Bandit security scan, and Docker Hub publish

Run locally:

1. Create virtualenv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```
