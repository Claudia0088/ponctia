// =====================================================
// CONFIGURATION
// =====================================================

const API_URL =
    "http://127.0.0.1:5000/api";


// =====================================================
// UTILISATEUR CONNECTÉ
// =====================================================

const userData =
    localStorage.getItem("ponctia_user");


if (!userData) {

    window.location.href = "login.html";

}


const user =
    JSON.parse(userData);


// =====================================================
// ÉLÉMENTS
// =====================================================

const latenessForm =
    document.getElementById("latenessForm");

const courseSelect =
    document.getElementById("course");

const message =
    document.getElementById("latenessMessage");


// =====================================================
// CHARGER LES COURS
// =====================================================

async function loadCourses() {

    try {

        const response =
            await fetch(
                `${API_URL}/courses/`
            );


        const data =
            await response.json();


        if (!data.success) {

            courseSelect.innerHTML = `
                <option value="">
                    Impossible de charger les cours
                </option>
            `;

            return;

        }


        courseSelect.innerHTML = `
            <option value="">
                Sélectionner un cours
            </option>
        `;


        data.courses.forEach(function(course) {

            const option =
                document.createElement("option");


            option.value =
                course.id;


            option.textContent =
                course.name;


            courseSelect.appendChild(option);

        });


    } catch (error) {

        console.error(error);


        courseSelect.innerHTML = `
            <option value="">
                Erreur de connexion
            </option>
        `;

    }

}


// =====================================================
// ENVOYER UN RETARD
// =====================================================

latenessForm.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        const latenessDate =
            document.getElementById(
                "latenessDate"
            ).value;


        const arrivalTime =
            document.getElementById(
                "arrivalTime"
            ).value;


        const duration =
            document.getElementById(
                "duration"
            ).value;


        const courseId =
            document.getElementById(
                "course"
            ).value;


        const reason =
            document.getElementById(
                "reason"
            ).value;


        const comment =
            document.getElementById(
                "comment"
            ).value.trim();


        try {

            const response =
                await fetch(
                    `${API_URL}/latenesses/`,
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            student_id:
                                user.id,

                            course_id:
                                Number(courseId),

                            lateness_date:
                                latenessDate,

                            arrival_time:
                                arrivalTime,

                            duration_minutes:
                                Number(duration),

                            reason:
                                reason,

                            comment:
                                comment

                        })

                    }
                );


            const data =
                await response.json();


            if (data.success) {

                message.textContent =
                    data.message;

                message.className =
                    "success-message";


                latenessForm.reset();

            } else {

                message.textContent =
                    data.message;

                message.className =
                    "error-message";

            }


        } catch (error) {

            console.error(error);


            message.textContent =
                "Impossible de contacter le serveur.";

            message.className =
                "error-message";

        }

    }
);


// =====================================================
// DÉCONNEXION
// =====================================================

const logoutButton =
    document.getElementById(
        "logoutButton"
    );


logoutButton.addEventListener(
    "click",
    function() {

        localStorage.removeItem(
            "ponctia_user"
        );

        window.location.href =
            "login.html";

    }
);


// =====================================================
// INITIALISATION
// =====================================================

loadCourses();