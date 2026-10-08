import sys
from pathlib import Path


# Ajouter le dossier backend au chemin Python
PROJECT_ROOT = Path(__file__).resolve().parent.parent
BACKEND_PATH = PROJECT_ROOT / "backend"

sys.path.insert(0, str(BACKEND_PATH))


from database import get_connection


def test_database_connection():
    connection = None

    try:
        connection = get_connection()

        if connection.is_connected():
            print("✅ Connexion à MySQL réussie !")
            print(f"✅ Base de données : {connection.database}")

    except Exception as error:
        print("❌ Erreur de connexion à MySQL :")
        print(error)

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            print("🔌 Connexion MySQL fermée.")


if __name__ == "__main__":
    test_database_connection()