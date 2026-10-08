import os

from dotenv import load_dotenv


# Charger les variables du fichier .env
load_dotenv()


class Config:
    # Configuration MySQL
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_NAME = os.getenv("DB_NAME", "ponctia")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")

    # Configuration Flask
    DEBUG = True