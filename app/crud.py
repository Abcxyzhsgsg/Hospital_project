from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def get_patients(db: Session):
    return db.query(models.Patient).all()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_doctor(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()

def get_doctors(db: Session):
    return db.query(models.Doctor).all()

def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def get_appointment(db: Session, appointment_id: int):
    return db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()

def get_appointments(db: Session):
    return db.query(models.Appointment).all()

def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    # Validate patient and doctor exist
    patient = get_patient(db, appointment.patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    doctor = get_doctor(db, appointment.doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    # Check overlap for the same doctor
    new_start = appointment.appointment_start
    new_end = appointment.appointment_end
    if new_start >= new_end:
        raise HTTPException(status_code=400, detail="Invalid appointment range")

    conflict = db.query(models.Appointment).filter(
        models.Appointment.doctor_id == appointment.doctor_id,
        models.Appointment.appointment_start < new_end,
        models.Appointment.appointment_end > new_start,
    ).first()

    if conflict:
        raise HTTPException(status_code=400, detail="Appointment overlaps with existing appointment")

    db_appt = models.Appointment(**appointment.dict())
    db.add(db_appt)
    db.commit()
    db.refresh(db_appt)
    return db_appt
