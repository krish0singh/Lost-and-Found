"""
decorators.py
-------------
Custom decorators used by our routes.

`login_required` protects a route so that only logged-in users can
access it. If a visitor who is not logged in tries to open the page,
they are redirected to the login page with a friendly flash message.
"""

from functools import wraps
from flask import session, redirect, url_for, flash, request


def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to continue.", "warning")
            return redirect(url_for("auth.login", next=request.path))
        return view_func(*args, **kwargs)
    return wrapped_view
