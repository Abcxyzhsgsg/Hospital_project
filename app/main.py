from fastapi import FastAPI
from .routers import patients, doctors, appointments
from .database import engine, Base
import os

app = FastAPI(title="Hospital Appointment API")

app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(appointments.router)

# Ensure tables created when running locally (Alembic should manage migrations)
if os.getenv("CREATE_DB_ON_STARTUP", "true").lower() in ("1", "true"):
    Base.metadata.create_all(bind=engine)
