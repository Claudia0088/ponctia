from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from config import Config
from routes.auth import auth_bp
from routes.latenesses import lateness_bp
from routes.courses import course_bp
from routes.statistics import statistics_bp
import os

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(lateness_bp)
app.register_blueprint(course_bp)
app.register_blueprint(statistics_bp)


# =========================
# FRONTEND
# =========================

FRONTEND_FOLDER = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "frontend")
)


@app.route("/")
def home():
    return send_from_directory(
        FRONTEND_FOLDER,
        "login.html"
    )


@app.route("/<path:filename>")
def frontend(filename):
    return send_from_directory(
        FRONTEND_FOLDER,
        filename
    )


# =========================
# API
# =========================

@app.route("/api/health")
def health_check():
    return jsonify({
        "application": "Ponctia",
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )