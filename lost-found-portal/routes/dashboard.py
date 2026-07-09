"""
dashboard.py
------------
Blueprint for the user Dashboard.

Shows:
    - Total number of Lost Items reported (site-wide)
    - Total number of Found Items reported (site-wide)
    - The logged-in user's own total posts (lost + found)
"""

from flask import Blueprint, render_template, session

from models import LostItem, FoundItem
from utils.decorators import login_required

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard_bp.route("/")
@login_required
def dashboard():
    user_id = session["user_id"]

    total_lost = LostItem.query.count()
    total_found = FoundItem.query.count()

    my_lost_count = LostItem.query.filter_by(user_id=user_id).count()
    my_found_count = FoundItem.query.filter_by(user_id=user_id).count()
    my_total_posts = my_lost_count + my_found_count

    recent_lost = (
        LostItem.query.filter_by(user_id=user_id)
        .order_by(LostItem.created_at.desc())
        .limit(5)
        .all()
    )
    recent_found = (
        FoundItem.query.filter_by(user_id=user_id)
        .order_by(FoundItem.created_at.desc())
        .limit(5)
        .all()
    )

    return render_template(
        "dashboard.html",
        total_lost=total_lost,
        total_found=total_found,
        my_lost_count=my_lost_count,
        my_found_count=my_found_count,
        my_total_posts=my_total_posts,
        recent_lost=recent_lost,
        recent_found=recent_found,
    )
