"""
models package
----------------
Re-exports `db` and all model classes so the rest of the app can simply do:

    from models import db, User, LostItem, FoundItem
"""

from extensions import db
from models.user import User
from models.lost_item import LostItem
from models.found_item import FoundItem

__all__ = ["db", "User", "LostItem", "FoundItem"]
