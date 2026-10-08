const API_URL = "http://127.0.0.1:5000/api";


const registerForm = document.getElementById("registerForm");

if (registerForm) {

    registerForm.addEventListener("submit", async function (event) {

        event.preventDefault();

        const firstName = document.getElementById("firstName").value.trim();
        const lastName = document.getElementById("lastName").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("confirmPassword").value;

        const message = document.getElementById("registerMessage");

        // Vérifier les mots de passe
        if (password !== confirmPassword) {

            message.textContent =
                "Les mots de passe ne correspondent pas.";

            message.className = "error-message";

            return;
        }

        try {

            const response = await fetch(`${API_URL}/auth/register`, {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    first_name: firstName,
                    last_name: lastName,
                    email: email,
                    password: password
                })
            });

            const data = await response.json();

            if (data.success) {

                message.textContent = data.message;
                message.className = "success-message";

                // Redirection vers la connexion
                setTimeout(() => {

                    window.location.href = "login.html";

                }, 1500);

            } else {

                message.textContent = data.message;
                message.className = "error-message";
            }

        } catch (error) {

            console.error(error);

            message.textContent =
                "Impossible de contacter le serveur. Vérifie que Ponctia est lancé.";

            message.className = "error-message";
        }

    });

}


// =====================================================
// CONNEXION
// =====================================================

const loginForm = document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener("submit", async function (event) {

        event.preventDefault();

        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value;

        const message = document.getElementById("loginMessage");

        try {

            const response = await fetch(`${API_URL}/auth/login`, {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    email: email,
                    password: password
                })
            });

            const data = await response.json();

            if (data.success) {

                message.textContent = data.message;
                message.className = "success-message";

                // Sauvegarder l'utilisateur connecté
                localStorage.setItem(
                    "ponctia_user",
                    JSON.stringify(data.user)
                );

                // Redirection vers le dashboard
                setTimeout(() => {

                    window.location.href = "dashboard.html";

                }, 1000);

            } else {

                message.textContent = data.message;
                message.className = "error-message";
            }

        } catch (error) {

            console.error(error);

            message.textContent =
                "Impossible de contacter le serveur.";

            message.className = "error-message";
        }

    });

}