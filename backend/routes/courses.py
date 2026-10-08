from flask import Blueprint, jsonify

from services.course_service import get_all_courses


course_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)


# =====================================================
# RÉCUPÉRER LES COURS
# =====================================================

@course_bp.route("/", methods=["GET"])
def get_courses():

    result = get_all_courses()

    if not result["success"]:

        return jsonify(result), 500

    return jsonify(result), 200