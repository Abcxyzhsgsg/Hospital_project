from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/doctors", tags=["doctors"])

@router.get("", response_model=List[schemas.DoctorRead])
def list_doctors(db: Session = Depends(get_db)):
    return crud.get_doctors(db)

@router.post("", response_model=schemas.DoctorRead, status_code=201)
def create_doctor(payload: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return crud.create_doctor(db, payload)

@router.get("/{doctor_id}", response_model=schemas.DoctorRead)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    d = crud.get_doctor(db, doctor_id)
    if not d:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return d
