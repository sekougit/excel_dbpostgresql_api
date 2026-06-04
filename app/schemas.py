from pydantic import BaseModel

class PersonneSchema(BaseModel):
    numero: int
    prenom_nom: str
    sexe: str
    age: int
    region: str
    departement: str

    class Config:
        from_attributes = True