# Ponctia

Ponctia est une application web de gestion des retards étudiants.

L'idée du projet est de permettre aux étudiants de déclarer facilement leurs retards et de retrouver leur historique, tout en donnant aux équipes pédagogiques des outils pour suivre et gérer ces informations.

Ce projet est réalisé dans le cadre de mon Bachelor Informatique, avec une spécialisation en Intelligence Artificielle.

## Fonctionnalités

### Étudiant

* Création d'un compte
* Connexion à l'application
* Déclaration d'un retard
* Choix du cours concerné
* Date et heure d'arrivée
* Durée du retard
* Motif du retard
* Ajout d'un commentaire
* Consultation de l'historique
* Filtrage des retards selon leur statut

### Gestion

L'application prévoit également un espace destiné aux enseignants et aux administrateurs afin de pouvoir gérer les étudiants, les cours et les retards.

Des statistiques permettent également d'avoir une vue globale sur les retards enregistrés.

## Technologies utilisées

### Backend

* Python
* Flask
* MySQL Connector
* Flask-CORS
* python-dotenv
* Werkzeug

### Frontend

* HTML
* CSS
* JavaScript
* Fetch API

### Base de données

* MySQL
* phpMyAdmin
* WAMP

### Outils

* Visual Studio Code
* Git
* GitHub

## Architecture

Le projet est organisé en plusieurs parties afin de séparer le frontend, le backend et la base de données.

```text
ponctia/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   │
│   ├── routes/
│   ├── services/
│   └── utils/
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── lateness.html
│   ├── history.html
│   ├── admin.html
│   │
│   ├── css/
│   └── js/
│
├── database/
│   └── schema.sql
│
├── tests/
│   ├── test_auth.py
│   ├── test_database.py
│   └── test_lateness.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── .env
```

Le fonctionnement général est le suivant :

```text
Frontend
   |
   | HTTP / JSON
   v
Backend Flask
   |
   | SQL
   v
Base de données MySQL
```

Le frontend communique avec l'API Flask, qui se charge de traiter les données et de communiquer avec la base de données.

## Base de données

La base de données utilisée par Ponctia s'appelle `ponctia`.

Elle contient notamment les tables :

* `users`
* `classes`
* `teachers`
* `courses`
* `latenesses`

Les relations entre ces tables permettent notamment de relier un étudiant à ses retards, aux cours concernés et aux enseignants.

Le script de création de la base de données se trouve dans :

```text
database/schema.sql
```

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/Claudia0088/ponctia.git
cd ponctia
```

### 2. Créer l'environnement virtuel

Sous Windows :

```powershell
python -m venv venv
```

Puis l'activer :

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Installer les dépendances

```powershell
pip install -r requirements.txt
```

## Configuration de MySQL

Créer une base de données appelée :

```text
ponctia
```

Puis importer le fichier :

```text
database/schema.sql
```

Créer ensuite un fichier `.env` à la racine du projet :

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ponctia
DB_USER=root
DB_PASSWORD=
```

Les informations présentes dans `.env` sont propres à l'environnement local et ne doivent pas être publiées sur GitHub.

## Lancer le projet

Depuis le dossier du projet :

```powershell
cd backend
python app.py
```

Le serveur démarre sur :

```text
http://127.0.0.1:5000
```

L'application peut ensuite être ouverte dans un navigateur à cette adresse.

## API

Quelques routes actuellement disponibles :

### Authentification

```text
POST /api/auth/register
POST /api/auth/login
```

### Retards

```text
POST /api/latenesses/
GET /api/latenesses/student/<student_id>
```

### Cours

```text
GET /api/courses/
```

### Statistiques

```text
GET /api/statistics/student/<student_id>
```

### Vérification du serveur

```text
GET /api/health
```

Cette dernière route permet notamment de vérifier que l'application fonctionne correctement.

## Tests

Les tests sont regroupés dans le dossier `tests`.

Ils permettent notamment de vérifier la connexion à la base de données, l'authentification et la gestion des retards.

Pour les lancer :

```powershell
python tests/test_database.py
python tests/test_auth.py
python tests/test_lateness.py
```

## Intelligence artificielle

L'intelligence artificielle fait partie des évolutions prévues pour Ponctia.

L'objectif est d'ajouter progressivement des fonctionnalités permettant notamment d'analyser les données de retards et d'identifier certaines tendances.

Cette partie sera développée dans une prochaine version du projet.

## Évolutions prévues

Le projet est encore en développement. Parmi les prochaines fonctionnalités envisagées :

* amélioration de l'espace administrateur ;
* gestion plus complète des enseignants ;
* gestion des justificatifs ;
* notifications ;
* export des données ;
* graphiques et statistiques plus détaillées ;
* amélioration de l'interface responsive ;
* ajout d'un mode sombre ;
* intégration de fonctionnalités d'intelligence artificielle ;
* amélioration des tests ;
* renforcement de la sécurité ;
* déploiement de l'application.

## Objectif

Ce projet me permet de mettre en pratique plusieurs compétences acquises pendant ma formation :

* développement web ;
* Python et Flask ;
* conception d'API ;
* gestion d'une base de données MySQL ;
* JavaScript ;
* authentification ;
* tests ;
* Git et GitHub ;
* conception d'une application avec une future intégration de l'intelligence artificielle.

## Projet

Ponctia est développé dans le cadre de mon Bachelor Informatique, spécialisation Intelligence Artificielle.

**Claudia DOGBE**

GitHub : https://github.com/Claudia0088/ponctia

## Statut

Projet en cours de développement.
