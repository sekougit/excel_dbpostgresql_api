import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Charger ton fichier
df = pd.read_excel("data/donnees.xlsx")

# IMPORTANT: correspondance exacte des colonnes
df.columns = [
    "numero",
    "prenom_nom",
    "sexe",
    "age",
    "region",
    "departement"
]

# Envoyer vers PostgreSQL
df.to_sql("donnees", engine, if_exists="replace", index=False)

print("Import terminé avec succès")