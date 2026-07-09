"""
app.py
------
Entry point of the Lost & Found Portal Flask application.

Run this file to start the development server:

    python app.py

This uses the "application factory" pattern (create_app) which is a
Flask best practice: it keeps configuration, extension setup, and
blueprint registration in one clear, readable place.
"""

import os
from datetime import datetime, timezone
from flask import Flask, render_template

from extensions import db
from models import LostItem, FoundItem

# Blueprints (each module's routes live in their own file)
from routes.auth import auth_bp
from routes.lost import lost_bp
from routes.found import found_bp
from routes.dashboard import dashboard_bp
from routes.search import search_bp

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)

    # ---------------------------------------------------------------
    # Configuration
    # ---------------------------------------------------------------
    app.config["SECRET_KEY"] = "change-this-secret-key-in-production"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        BASE_DIR, "database.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ---------------------------------------------------------------
    # Extensions
    # ---------------------------------------------------------------
    db.init_app(app)

    # ---------------------------------------------------------------
    # Blueprints (feature modules)
    # ---------------------------------------------------------------
    app.register_blueprint(auth_bp)
    app.register_blueprint(lost_bp)
    app.register_blueprint(found_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(search_bp)

    # ---------------------------------------------------------------
    # Home page route (kept here since it's the app's landing page,
    # not tied to a single feature module)
    # ---------------------------------------------------------------
    @app.route("/")
    def home():
        latest_lost = LostItem.query.order_by(LostItem.created_at.desc()).limit(6).all()
        latest_found = FoundItem.query.order_by(FoundItem.created_at.desc()).limit(6).all()
        return render_template("home.html", latest_lost=latest_lost, latest_found=latest_found)

    # ---------------------------------------------------------------
    # Error handlers
    # ---------------------------------------------------------------
    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    @app.errorhandler(403)
    def forbidden(e):
        return render_template("403.html"), 403

    # Make `now()` available in every template (used in footer for copyright year)
    @app.context_processor
    def inject_now():
        return {"current_year": datetime.now(timezone.utc).year}

    # ---------------------------------------------------------------
    # Create database tables if they don't exist yet
    # ---------------------------------------------------------------
    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
