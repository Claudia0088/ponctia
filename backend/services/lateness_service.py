from database import get_connection


def create_lateness(
    student_id,
    course_id,
    lateness_date,
    arrival_time,
    duration_minutes,
    reason,
    comment
):
    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute("""
            INSERT INTO latenesses
            (
                student_id,
                course_id,
                lateness_date,
                arrival_time,
                duration_minutes,
                reason,
                comment,
                status
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                'pending'
            )
        """, (
            student_id,
            course_id,
            lateness_date,
            arrival_time,
            duration_minutes,
            reason,
            comment
        ))

        connection.commit()

        return {
            "success": True,
            "message": "Retard enregistré avec succès.",
            "lateness_id": cursor.lastrowid
        }

    except Exception as error:

        connection.rollback()

        print("Erreur lors de l'enregistrement du retard :")
        print(error)

        return {
            "success": False,
            "message": "Impossible d'enregistrer le retard."
        }

    finally:

        cursor.close()
        connection.close()


def get_student_latenesses(student_id):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT
                latenesses.id,
                latenesses.lateness_date,
                latenesses.arrival_time,
                latenesses.duration_minutes,
                latenesses.reason,
                latenesses.comment,
                latenesses.status,
                latenesses.created_at,

                courses.name AS course_name,

                teachers.first_name AS teacher_first_name,
                teachers.last_name AS teacher_last_name

            FROM latenesses

            LEFT JOIN courses
                ON latenesses.course_id = courses.id

            LEFT JOIN teachers
                ON courses.teacher_id = teachers.id

            WHERE latenesses.student_id = %s

            ORDER BY
                latenesses.lateness_date DESC,
                latenesses.arrival_time DESC

        """, (student_id,))


        latenesses = cursor.fetchall()


        # ==================================================
        # CONVERSION DES TYPES MYSQL POUR JSON
        # ==================================================

        for lateness in latenesses:

            # MySQL TIME est retourné par Python
            # sous forme de timedelta.
            # On le convertit en HH:MM:SS.

            if lateness["arrival_time"] is not None:

                total_seconds = int(
                    lateness["arrival_time"].total_seconds()
                )

                hours = total_seconds // 3600

                minutes = (
                    total_seconds % 3600
                ) // 60

                seconds = (
                    total_seconds % 60
                )

                lateness["arrival_time"] = (
                    f"{hours:02d}:"
                    f"{minutes:02d}:"
                    f"{seconds:02d}"
                )


            # Conversion de la date pour JSON

            if lateness["lateness_date"] is not None:

                lateness["lateness_date"] = (
                    lateness["lateness_date"].isoformat()
                )


            # Conversion de created_at

            if lateness["created_at"] is not None:

                lateness["created_at"] = (
                    lateness["created_at"].isoformat()
                )


        return {
            "success": True,
            "latenesses": latenesses
        }


    except Exception as error:

        print(
            "Erreur lors de la récupération des retards :"
        )

        print(error)

        return {
            "success": False,
            "message": "Impossible de récupérer les retards."
        }


    finally:

        cursor.close()
        connection.close()