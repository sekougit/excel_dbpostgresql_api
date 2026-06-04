from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from .database import SessionLocal, engine, Base
from .models import Personne
from .schemas import PersonneSchema
from .crud import get_all, get_by_region, get_by_age

# création des tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Données Excel")

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home
@app.get("/")
def home():
    return {"message": "API opérationnelle"}

# Tous les enregistrements
@app.get("/personnes", response_model=List[PersonneSchema])
def read_all(db: Session = Depends(get_db)):
    return get_all(db)

# Filtre par région
@app.get("/personnes/region/{region}", response_model=List[PersonneSchema])
def by_region(region: str, db: Session = Depends(get_db)):
    return get_by_region(db, region)

# Filtre par âge
@app.get("/personnes/age/{age}", response_model=List[PersonneSchema])
def by_age(age: int, db: Session = Depends(get_db)):
    return get_by_age(db, age)