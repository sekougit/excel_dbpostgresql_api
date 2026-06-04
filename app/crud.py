from .models import Personne

def get_all(db):
    return db.query(Personne).all()


def get_by_region(db, region):
    return db.query(Personne).filter(Personne.region == region).all()


def get_by_age(db, age):
    return db.query(Personne).filter(Personne.age == age).all()