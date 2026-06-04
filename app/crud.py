from sqlalchemy.orm import Session
from .models import Personne

def get_all(db: Session):
    return db.query(Personne).all()

def get_by_region(db: Session, region: str):
    return db.query(Personne).filter(Personne.region == region).all()

def get_by_age(db: Session, age: int):
    return db.query(Personne).filter(Personne.age == age).all()