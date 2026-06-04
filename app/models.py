from sqlalchemy import Column, Integer, String
from database import Base

class Personne(Base):
    __tablename__ = "donnees"

    numero = Column(Integer, primary_key=True, index=True)
    prenom_nom = Column(String)
    sexe = Column(String)
    age = Column(Integer)
    region = Column(String)
    departement = Column(String)