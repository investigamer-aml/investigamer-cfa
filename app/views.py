"""
 Module to handle all the views of the app
"""

from datetime import datetime, timezone

from flask import Blueprint
from flask import current_app as app
from flask import jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from dbb.models import UseCases, Users, db

auth_bp = Blueprint("auth", __name__)


##### REGISTRATION #####
@app.route("/register", methods=["POST"])
def register():
    """
    Handle the user registration process. Collects data from form, validates,
    creates a new user, and then redirects to the login page.
    """
    data = request.get_json()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    password = data.get("password")
    is_admin = data.get("is_admin", False)

    # Check if user already exists
    user_exists = Users.query.filter(
        (Users.email == email)
        | (Users.first_name == first_name)
        | (Users.last_name == last_name)
    ).first()
    if user_exists:
        return jsonify({"error": "User already exists"}), 400

    # Create new user
    new_user = Users(
        first_name=first_name,
        last_name=last_name,
        email=email,
        is_admin=is_admin,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
    )
    new_user.set_password(password)  # Hash password

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


@app.route("/register", methods=["GET"])
def show_register():
    """
    Display the registration page.
    """
    return render_template("register.html")


####### LOGIN #######
@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate the user. If authentication is successful, redirect to the homepage;
    otherwise, return an error.
    """
    if current_user.is_authenticated:
        return redirect(url_for("home"))  # Redirect to the homepage

    login_input = request.form.get(
        "login_input"
    )  # Assuming you change the form to have 'login_input' instead of 'username'
    password = request.form.get("password")

    # Attempt to authenticate first by username, then by email
    user = Users.query.filter(
        (Users.username == login_input) | (Users.email == login_input)
    ).first()

    if user and user.check_password(password):
        login_user(user)
        return redirect(url_for("home"))  # Redirect to the homepage
    else:
        return jsonify({"error": "Invalid username or password"}), 401


@app.route("/login", methods=["GET"])
def show_login():
    """
    Display the login page.
    """
    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    """
    Log the user out
    """
    logout_user()
    return redirect(url_for("main.home"))


@app.route("/admin")
@login_required
def admin():
    """
    Display the admin page with a list of use cases created by the current logged-in user, filtered by type.
    """
    # Retrieve a type filter from query parameters (if any)
    type_filter = request.args.get("type")

    if type_filter:
        use_cases = UseCases.query.filter_by(
            created_by_user=current_user.id, type=type_filter
        ).all()
    else:
        use_cases = UseCases.query.filter_by(created_by_user=current_user.id).all()

    return render_template("admin.html", use_cases=use_cases)
