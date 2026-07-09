"""
found.py
--------
Blueprint for the Found Item module.

Logged-in users can:
    - Add a found item
    - View ALL found items (so anyone can spot an item that might be theirs)
"""

from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, session, flash

from extensions import db
from models import FoundItem
from utils.decorators import login_required
from utils.validators import validate_item_form, CATEGORIES

found_bp = Blueprint("found", __name__, url_prefix="/found")


@found_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_found():
    if request.method == "POST":
        errors = validate_item_form(request.form)

        if errors:
            for e in errors:
                flash(e, "danger")
            return render_template("add_found.html", categories=CATEGORIES, form=request.form)

        item = FoundItem(
            user_id=session["user_id"],
            item_name=request.form["item_name"].strip(),
            category=request.form["category"],
            description=request.form.get("description", "").strip(),
            location=request.form["location"].strip(),
            date=datetime.strptime(request.form["date"], "%Y-%m-%d").date(),
            contact=request.form["contact"].strip(),
        )
        db.session.add(item)
        db.session.commit()

        flash("Found item reported successfully! Thank you for helping out.", "success")
        return redirect(url_for("found.view_found"))

    return render_template("add_found.html", categories=CATEGORIES)


@found_bp.route("/view")
@login_required
def view_found():
    # All found items are visible to every logged-in user, so the
    # original owner has the best chance of spotting their item.
    items = FoundItem.query.order_by(FoundItem.created_at.desc()).all()
    return render_template("view_found.html", items=items)
