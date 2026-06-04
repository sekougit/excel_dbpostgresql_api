from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import Personne
from .crud import get_all, get_by_region, get_by_age

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Données Excel")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "API opérationnelle"}

# Tous les enregistrements
@app.get("/personnes")
def read_all(db: Session = Depends(get_db)):
    return get_all(db)

# Filtre par région
@app.get("/personnes/region/{region}")
def by_region(region: str, db: Session = Depends(get_db)):
    return get_by_region(db, region)

# Filtre par âge
@app.get("/personnes/age/{age}")
def by_age(age: int, db: Session = Depends(get_db)):
    return get_by_age(db, age)