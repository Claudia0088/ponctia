from database import get_connection
from utils.security import hash_password, verify_password


def register_user(first_name, last_name, email, password):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # Vérifier si l'adresse email existe déjà
        cursor.execute(
            "SELECT id FROM users WHERE email = %s",
            (email,)
        )

        existing_user = cursor.fetchone()

        if existing_user:
            return {
                "success": False,
                "message": "Cette adresse email est déjà utilisée."
            }

        # Créer le mot de passe sécurisé
        password_hash = hash_password(password)

        # Créer l'utilisateur
        cursor.execute(
            """
            INSERT INTO users
            (first_name, last_name, email, password_hash, role)
            VALUES (%s, %s, %s, %s, 'student')
            """,
            (first_name, last_name, email, password_hash)
        )

        connection.commit()

        return {
            "success": True,
            "message": "Compte étudiant créé avec succès.",
            "user_id": cursor.lastrowid
        }

    finally:
        cursor.close()
        connection.close()


def login_user(email, password):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT id, first_name, last_name, email, password_hash, role
            FROM users
            WHERE email = %s
            """,
            (email,)
        )

        user = cursor.fetchone()

        if not user:
            return {
                "success": False,
                "message": "Email ou mot de passe incorrect."
            }

        if not verify_password(password, user["password_hash"]):
            return {
                "success": False,
                "message": "Email ou mot de passe incorrect."
            }

        return {
            "success": True,
            "message": "Connexion réussie.",
            "user": {
                "id": user["id"],
                "first_name": user["first_name"],
                "last_name": user["last_name"],
                "email": user["email"],
                "role": user["role"]
            }
        }

    finally:
        cursor.close()
        connection.close()