from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/peppers", endpoint='peppers')
def about():
    return render_template("pages/peppers.html")

@bp.route("/words", endpoint='words')
def about():
    return render_template("pages/words.html")
