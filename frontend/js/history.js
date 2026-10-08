const API_URL = "http://127.0.0.1:5000/api";


// =====================================================
// VÉRIFICATION DE LA CONNEXION
// =====================================================

const userData = localStorage.getItem("ponctia_user");

if (!userData) {

    window.location.href = "login.html";

} else {

    const user = JSON.parse(userData);


    // =====================================================
    // ÉLÉMENTS HTML
    // =====================================================

    const latenessForm =
        document.getElementById("latenessForm");

    const courseSelect =
        document.getElementById("course");

    const message =
        document.getElementById("latenessMessage");

    const logoutButton =
        document.getElementById("logoutButton");


    // =====================================================
    // CHARGER LES COURS
    // =====================================================

    async function loadCourses() {

        try {

            const response =
                await fetch(
                    `${API_URL}/courses/`
                );


            if (!response.ok) {

                throw new Error(
                    `Erreur HTTP ${response.status}`
                );

            }


            const data =
                await response.json();


            if (!data.success) {

                courseSelect.innerHTML =
                    `<option value="">
                        Impossible de charger les cours
                    </option>`;

                return;

            }


            courseSelect.innerHTML =
                `<option value="">
                    Sélectionner un cours
                </option>`;


            data.courses.forEach(
                function(course) {

                    const option =
                        document.createElement("option");


                    option.value =
                        course.id;


                    option.textContent =
                        course.name;


                    courseSelect.appendChild(
                        option
                    );

                }
            );


        } catch (error) {

            console.error(
                "Erreur lors du chargement des cours :",
                error
            );


            courseSelect.innerHTML =
                `<option value="">
                    Erreur de connexion au serveur
                </option>`;

        }

    }


    // =====================================================
    // ENREGISTRER UN RETARD
    // =====================================================

    latenessForm.addEventListener(
        "submit",
        async function(event) {

            event.preventDefault();


            // ---------------------------------------------
            // RÉCUPÉRATION DES VALEURS
            // ---------------------------------------------

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


            // ---------------------------------------------
            // VÉRIFICATION
            // ---------------------------------------------

            if (
                !latenessDate ||
                !arrivalTime ||
                !duration ||
                !courseId ||
                !reason
            ) {

                message.textContent =
                    "Merci de remplir tous les champs obligatoires.";

                message.className =
                    "error-message";

                return;

            }


            // ---------------------------------------------
            // DÉSACTIVER LE BOUTON
            // ---------------------------------------------

            const submitButton =
                latenessForm.querySelector(
                    "button[type='submit']"
                );


            submitButton.disabled = true;

            submitButton.textContent =
                "Enregistrement...";


            try {

                // -----------------------------------------
                // ENVOI AU BACKEND
                // -----------------------------------------

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
                                    Number(user.id),

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


                // -----------------------------------------
                // VÉRIFIER LA RÉPONSE
                // -----------------------------------------

                if (!response.ok) {

                    throw new Error(
                        `Erreur HTTP ${response.status}`
                    );

                }


                const data =
                    await response.json();


                console.log(
                    "Réponse du serveur :",
                    data
                );


                // -----------------------------------------
                // SUCCÈS
                // -----------------------------------------

                if (data.success) {

                    message.textContent =
                        "Retard enregistré avec succès.";

                    message.className =
                        "success-message";


                    latenessForm.reset();


                    // Recharger les cours après reset
                    loadCourses();


                    // Redirection vers l'historique
                    setTimeout(
                        function() {

                            window.location.href =
                                "history.html";

                        },
                        1200
                    );


                } else {

                    message.textContent =
                        data.message ||
                        "Impossible d'enregistrer le retard.";

                    message.className =
                        "error-message";

                }


            } catch (error) {

                console.error(
                    "Erreur lors de l'enregistrement :",
                    error
                );


                message.textContent =
                    "Impossible de contacter le serveur.";

                message.className =
                    "error-message";


            } finally {

                submitButton.disabled = false;

                submitButton.textContent =
                    "Déclarer mon retard";

            }

        }
    );


    // =====================================================
    // DÉCONNEXION
    // =====================================================

    if (logoutButton) {

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

    }


    // =====================================================
    // DÉMARRAGE
    // =====================================================

    loadCourses();

}