from database import get_connection


# =====================================================
# STATISTIQUES D'UN ÉTUDIANT
# =====================================================

def get_student_statistics(student_id):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    try:

        # -------------------------------------------------
        # TOTAL
        # -------------------------------------------------

        cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM latenesses
            WHERE student_id = %s
            """,
            (student_id,)
        )

        total = cursor.fetchone()["total"]


        # -------------------------------------------------
        # EN ATTENTE
        # -------------------------------------------------

        cursor.execute(
            """
            SELECT COUNT(*) AS pending
            FROM latenesses
            WHERE student_id = %s
            AND status = 'pending'
            """,
            (student_id,)
        )

        pending = cursor.fetchone()["pending"]


        # -------------------------------------------------
        # JUSTIFIÉS
        # -------------------------------------------------

        cursor.execute(
            """
            SELECT COUNT(*) AS justified
            FROM latenesses
            WHERE student_id = %s
            AND status = 'justified'
            """,
            (student_id,)
        )

        justified = cursor.fetchone()["justified"]


        # -------------------------------------------------
        # REFUSÉS
        # -------------------------------------------------

        cursor.execute(
            """
            SELECT COUNT(*) AS rejected
            FROM latenesses
            WHERE student_id = %s
            AND status = 'rejected'
            """,
            (student_id,)
        )

        rejected = cursor.fetchone()["rejected"]


        # -------------------------------------------------
        # TEMPS TOTAL DE RETARD
        # -------------------------------------------------

        cursor.execute(
            """
            SELECT COALESCE(SUM(duration_minutes), 0) AS total_minutes
            FROM latenesses
            WHERE student_id = %s
            """,
            (student_id,)
        )

        total_minutes = cursor.fetchone()["total_minutes"]


        return {

            "success": True,

            "statistics": {

                "total": total,

                "pending": pending,

                "justified": justified,

                "rejected": rejected,

                "total_minutes": total_minutes

            }

        }

    except Exception as error:

        print("Erreur statistiques :")
        print(error)

        return {

            "success": False,

            "message": "Impossible de récupérer les statistiques."

        }

    finally:

        cursor.close()

        connection.close()