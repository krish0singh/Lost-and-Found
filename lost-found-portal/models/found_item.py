"""
FoundItem model
---------------
Represents an item that a user has FOUND and wants to return to its owner.
"""

from datetime import datetime, timezone
from extensions import db


class FoundItem(db.Model):
    __tablename__ = "found_items"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    item_name = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(150), nullable=False)   # Found Location
    date = db.Column(db.Date, nullable=False)               # Found Date
    contact = db.Column(db.String(20), nullable=False)      # Contact Number

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<FoundItem {self.item_name}>"
