"""
User model
----------
Stores registered users of the Lost & Found Portal.
Passwords are NEVER stored in plain text -- they are hashed using
Werkzeug's security helpers (see routes/auth.py).
"""

from datetime import datetime, timezone
from extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # hashed password
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships: one user can have many lost items and many found items
    lost_items = db.relationship(
        "LostItem", backref="owner", lazy=True, cascade="all, delete-orphan"
    )
    found_items = db.relationship(
        "FoundItem", backref="owner", lazy=True, cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.username}>"
