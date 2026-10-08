from flask import Blueprint, jsonify

from services.statistics_service import get_student_statistics


statistics_bp = Blueprint(
    "statistics",
    __name__,
    url_prefix="/api/statistics"
)


# =====================================================
# STATISTIQUES ÉTUDIANT
# =====================================================

@statistics_bp.route("/student/<int:student_id>", methods=["GET"])
def student_statistics(student_id):

    result = get_student_statistics(student_id)

    if not result["success"]:

        return jsonify(result), 500

    return jsonify(result), 200