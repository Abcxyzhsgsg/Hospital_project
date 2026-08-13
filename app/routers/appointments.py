from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/appointments", tags=["appointments"])

@router.get("", response_model=List[schemas.AppointmentRead])
def list_appointments(db: Session = Depends(get_db)):
    return crud.get_appointments(db)

@router.post("", response_model=schemas.AppointmentRead, status_code=201)
def create_appointment(payload: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return crud.create_appointment(db, payload)

@router.get("/{appointment_id}", response_model=schemas.AppointmentRead)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    a = crud.get_appointment(db, appointment_id)
    if not a:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return a
