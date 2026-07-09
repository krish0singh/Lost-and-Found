"""
lost.py
-------
Blueprint for the Lost Item module.

Logged-in users can:
    - Add a lost item
    - View their own lost items
    - Edit their own lost item
    - Delete their own lost item
"""

from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, abort

from extensions import db
from models import LostItem
from utils.decorators import login_required
from utils.validators import validate_item_form, CATEGORIES

lost_bp = Blueprint("lost", __name__, url_prefix="/lost")


@lost_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_lost():
    if request.method == "POST":
        errors = validate_item_form(request.form)

        if errors:
            for e in errors:
                flash(e, "danger")
            return render_template("add_lost.html", categories=CATEGORIES, form=request.form)

        item = LostItem(
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

        flash("Lost item reported successfully!", "success")
        return redirect(url_for("lost.view_lost"))

    return render_template("add_lost.html", categories=CATEGORIES)


@lost_bp.route("/view")
@login_required
def view_lost():
    items = (
        LostItem.query.filter_by(user_id=session["user_id"])
        .order_by(LostItem.created_at.desc())
        .all()
    )
    return render_template("view_lost.html", items=items)


@lost_bp.route("/edit/<int:item_id>", methods=["GET", "POST"])
@login_required
def edit_lost(item_id):
    item = LostItem.query.get_or_404(item_id)

    if item.user_id != session["user_id"]:
        abort(403)

    if request.method == "POST":
        errors = validate_item_form(request.form)

        if errors:
            for e in errors:
                flash(e, "danger")
            return render_template("edit_lost.html", item=item, categories=CATEGORIES)

        item.item_name = request.form["item_name"].strip()
        item.category = request.form["category"]
        item.description = request.form.get("description", "").strip()
        item.location = request.form["location"].strip()
        item.date = datetime.strptime(request.form["date"], "%Y-%m-%d").date()
        item.contact = request.form["contact"].strip()

        db.session.commit()
        flash("Lost item updated successfully!", "success")
        return redirect(url_for("lost.view_lost"))

    return render_template("edit_lost.html", item=item, categories=CATEGORIES)


@lost_bp.route("/delete/<int:item_id>", methods=["POST"])
@login_required
def delete_lost(item_id):
    item = LostItem.query.get_or_404(item_id)

    if item.user_id != session["user_id"]:
        abort(403)

    db.session.delete(item)
    db.session.commit()
    flash("Lost item deleted.", "info")
    return redirect(url_for("lost.view_lost"))
