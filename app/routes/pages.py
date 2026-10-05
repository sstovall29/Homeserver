from flask import Blueprint, render_template, redirect, request

pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/")
def home():
    return render_template("home.html")

@pages_bp.route("/about")
def about():
    return render_template("about.html")

@pages_bp.route("/ble_presence")
def ble_presence():
    return render_template("ble_presence.html")

@pages_bp.route("/form")
def form():
    return render_template("form.html")

@pages_bp.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    print(username)
    return redirect("/form")