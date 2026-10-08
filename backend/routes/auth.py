from flask import Blueprint, request, jsonify

from services.auth_service import register_user, login_user


auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Aucune donnée reçue."
        }), 400

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    password = data.get("password")

    if not all([first_name, last_name, email, password]):
        return jsonify({
            "success": False,
            "message": "Tous les champs sont obligatoires."
        }), 400

    result = register_user(
        first_name,
        last_name,
        email,
        password
    )

    if not result["success"]:
        return jsonify(result), 409

    return jsonify(result), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Aucune donnée reçue."
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "success": False,
            "message": "L'email et le mot de passe sont obligatoires."
        }), 400

    result = login_user(email, password)

    if not result["success"]:
        return jsonify(result), 401

    return jsonify(result), 200