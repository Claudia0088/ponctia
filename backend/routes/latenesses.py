from flask import Blueprint, request, jsonify

from services.lateness_service import (
    create_lateness,
    get_student_latenesses
)


lateness_bp = Blueprint(
    "latenesses",
    __name__,
    url_prefix="/api/latenesses"
)


# =====================================================
# CRÉER UN RETARD
# =====================================================

@lateness_bp.route("/", methods=["POST"])
def create():

    data = request.get_json()


    if not data:

        return jsonify({

            "success": False,

            "message": "Aucune donnée reçue."

        }), 400


    student_id = data.get("student_id")

    course_id = data.get("course_id")

    lateness_date = data.get("lateness_date")

    arrival_time = data.get("arrival_time")

    duration_minutes = data.get("duration_minutes")

    reason = data.get("reason")

    comment = data.get("comment")


    if not all([
        student_id,
        course_id,
        lateness_date,
        arrival_time,
        duration_minutes,
        reason
    ]):

        return jsonify({

            "success": False,

            "message": "Les champs obligatoires sont manquants."

        }), 400


    result = create_lateness(

        student_id,

        course_id,

        lateness_date,

        arrival_time,

        duration_minutes,

        reason,

        comment

    )


    if not result["success"]:

        return jsonify(result), 500


    return jsonify(result), 201


# =====================================================
# HISTORIQUE ÉTUDIANT
# =====================================================

@lateness_bp.route(
    "/student/<int:student_id>",
    methods=["GET"]
)
def get_student_history(student_id):

    result = get_student_latenesses(student_id)


    if not result["success"]:

        return jsonify(result), 500


    return jsonify(result), 200