import mysql.connector

from config import Config


def get_connection():
    """
    Crée une connexion avec la base de données MySQL.
    """

    connection = mysql.connector.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        database=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )

    return connection