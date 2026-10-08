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
// INFORMATIONS UTILISATEUR
// =====================================================

document.getElementById(
    "studentName"
).textContent =
    user.first_name;


document.getElementById(
    "profileFirstName"
).textContent =
    user.first_name;


document.getElementById(
    "profileLastName"
).textContent =
    user.last_name;


document.getElementById(
    "profileEmail"
).textContent =
    user.email;


document.getElementById(
    "profileRole"
).textContent =
    user.role;


// =====================================================
// CHARGER LES STATISTIQUES
// =====================================================

async function loadStatistics() {

    try {

        const response =
            await fetch(
                `${API_URL}/statistics/student/${user.id}`
            );


        const data =
            await response.json();


        if (!data.success) {

            console.error(
                data.message
            );

            return;

        }


        const stats =
            data.statistics;


        document.getElementById(
            "totalLateness"
        ).textContent =
            stats.total;


        document.getElementById(
            "pendingLateness"
        ).textContent =
            stats.pending;


        document.getElementById(
            "justifiedLateness"
        ).textContent =
            stats.justified;


        document.getElementById(
            "rejectedLateness"
        ).textContent =
            stats.rejected;

    } catch (error) {

        console.error(
            "Erreur statistiques :",
            error
        );

    }

}


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

loadStatistics();