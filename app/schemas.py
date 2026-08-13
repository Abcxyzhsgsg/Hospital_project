from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PatientCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

class PatientRead(PatientCreate):
    id: int
    class Config:
        orm_mode = True

class DoctorCreate(BaseModel):
    name: str
    specialization: Optional[str] = None

class DoctorRead(DoctorCreate):
    id: int
    class Config:
        orm_mode = True

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_start: datetime
    appointment_end: datetime

class AppointmentRead(AppointmentCreate):
    id: int
    class Config:
        orm_mode = True
