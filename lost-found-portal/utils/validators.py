"""
validators.py
-------------
Small, dependency-free helper functions for validating form input on
the server side. We deliberately avoid extra libraries (like
Flask-WTF) to keep the project simple and easy to understand for a
mini project, while still validating every field properly.
"""

import re
from datetime import datetime

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PHONE_REGEX = re.compile(r"^[0-9]{7,15}$")

CATEGORIES = [
    "Electronics",
    "Documents",
    "Accessories",
    "Bags",
    "Clothing",
    "Keys",
    "Books",
    "Others",
]


def is_valid_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email or ""))


def is_valid_phone(phone: str) -> bool:
    return bool(PHONE_REGEX.match((phone or "").strip()))


def is_valid_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False


def validate_item_form(form):
    """
    Validates the fields shared by the Lost Item and Found Item forms.
    Returns a list of error messages (empty list means the form is valid).
    """
    errors = []

    item_name = form.get("item_name", "").strip()
    category = form.get("category", "").strip()
    location = form.get("location", "").strip()
    date = form.get("date", "").strip()
    contact = form.get("contact", "").strip()

    if not item_name or len(item_name) < 2:
        errors.append("Item name must be at least 2 characters long.")

    if category not in CATEGORIES:
        errors.append("Please select a valid category.")

    if not location:
        errors.append("Location is required.")

    if not is_valid_date(date):
        errors.append("Please provide a valid date (YYYY-MM-DD).")

    if not is_valid_phone(contact):
        errors.append("Contact number must be 7-15 digits.")

    return errors
