"""
search.py
---------
Blueprint for the Search module.

Users can search across BOTH Lost and Found items by:
    - Item Name
    - Category
"""

from flask import Blueprint, render_template, request

from models import LostItem, FoundItem
from utils.decorators import login_required
from utils.validators import CATEGORIES

search_bp = Blueprint("search", __name__, url_prefix="/search")


@search_bp.route("/")
@login_required
def search():
    keyword = request.args.get("keyword", "").strip()
    category = request.args.get("category", "").strip()

    lost_query = LostItem.query
    found_query = FoundItem.query

    if keyword:
        like_pattern = f"%{keyword}%"
        lost_query = lost_query.filter(LostItem.item_name.ilike(like_pattern))
        found_query = found_query.filter(FoundItem.item_name.ilike(like_pattern))

    if category:
        lost_query = lost_query.filter(LostItem.category == category)
        found_query = found_query.filter(FoundItem.category == category)

    lost_results = lost_query.order_by(LostItem.created_at.desc()).all()
    found_results = found_query.order_by(FoundItem.created_at.desc()).all()

    searched = bool(keyword or category)

    return render_template(
        "search_results.html",
        lost_results=lost_results,
        found_results=found_results,
        keyword=keyword,
        category=category,
        categories=CATEGORIES,
        searched=searched,
    )
