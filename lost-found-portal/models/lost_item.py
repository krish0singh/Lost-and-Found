"""
LostItem model
--------------
Represents an item that a user has LOST and is looking for.
"""

from datetime import datetime, timezone
from extensions import db


class LostItem(db.Model):
    __tablename__ = "lost_items"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    item_name = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(150), nullable=False)   # Lost Location
    date = db.Column(db.Date, nullable=False)               # Lost Date
    contact = db.Column(db.String(20), nullable=False)      # Contact Number

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<LostItem {self.item_name}>"
