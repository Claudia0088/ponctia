from database import get_connection


# =====================================================
# RÉCUPÉRER TOUS LES COURS
# =====================================================

def get_all_courses():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    try:

        cursor.execute(
            """
            SELECT
                courses.id,
                courses.name,
                teachers.id AS teacher_id,
                teachers.first_name AS teacher_first_name,
                teachers.last_name AS teacher_last_name

            FROM courses

            LEFT JOIN teachers
                ON courses.teacher_id = teachers.id

            ORDER BY courses.name ASC
            """
        )

        courses = cursor.fetchall()

        return {
            "success": True,
            "courses": courses
        }

    except Exception as error:

        print("Erreur lors de la récupération des cours :")
        print(error)

        return {
            "success": False,
            "message": "Impossible de récupérer les cours."
        }

    finally:

        cursor.close()
        connection.close()