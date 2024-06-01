from datetime import datetime
from typing import Any, Dict, Optional

import markdown
from flask import Flask
from flask import current_app as app
from flask import jsonify, redirect, render_template, request, session, url_for
from flask_login import (LoginManager, UserMixin, current_user, login_required,
                         login_user, logout_user)
from sqlalchemy.sql import func

from app import db
from dbb.models import (DifficultyLevel, Lessons, Options, Questions, UseCases,
                        UserAnswers, UserLessonInteraction, Users)

login_manager = LoginManager()
login_manager.init_app(app)


##### REGISTRATION #####
@app.route("/register", methods=["POST"])
def register():
    """
    Handle the user registration process. Collects data from form, validates,
    creates a new user, and then redirects to the login page.
    """
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    is_admin = "is_admin" in request.form

    # Check if user already exists
    user_exists = Users.query.filter(
        (Users.email == email) | (Users.username == username)
    ).first()
    if user_exists:
        return jsonify({"error": "User already exists"}), 400

    # Create new user
    new_user = Users(username=username, email=email, is_admin=is_admin)
    new_user.set_password(password)  # Hash password
    new_user.is_admin = is_admin  # Setting the is_admin flag based on checkbox
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("login"))  # Redirect to the login page


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


@app.route("/logout")
def logout():
    """
    Log out the current user and redirect to the home page.
    """
    logout_user()
    return redirect(url_for("home"))


@app.route("/login", methods=["GET"])
def show_login():
    """
    Display the login page.
    """
    return render_template("login.html")


@login_manager.user_loader
def load_user(user_id):
    """
    Load the user object from the user ID stored in the session.
    """
    return Users.query.get(int(user_id))


@app.route("/profile")
@login_required
def profile():
    """
    Display the profile page for the current user.
    """
    # Assuming you have a user object in the session
    return render_template("profile.html", user=current_user)


@app.route("/")
def home():
    """
    Display the homepage.
    """
    return render_template("index.html")


# Define your models based on the provided schema
@app.route("/practice/<int:lesson_id>")
@app.route("/practice")
def start_lesson():
    user_id = current_user.id

    # Check if there is a similar use case ID stored in the session
    similar_use_case_id = session.get("similar_use_case_id")
    if similar_use_case_id:
        # Retrieve the similar use case from the database
        use_case = UseCases.query.get(similar_use_case_id)
        if use_case:
            # Remove the similar use case ID from the session
            session.pop("similar_use_case_id", None)
            is_similar_use_case = True
    else:
        current_lesson = get_current_lesson(user_id)
        if current_lesson:
            current_use_case = get_current_use_case(user_id, current_lesson["id"])
            total_use_cases = get_lessons_use_case_count(current_lesson["id"])
            correct_use_cases = get_users_correct_use_cases_per_lesson(current_lesson["id"], user_id)

            if current_use_case:
                use_case = current_use_case
                is_similar_use_case = False
            else:
                # Move on to the next lesson
                next_lesson = get_next_lesson(user_id)
                if next_lesson:
                    use_case = next_lesson["use_cases"][
                        0
                    ]  # Retrieve the first use case of the next lesson
                    is_similar_use_case = False
                else:
                    # No more lessons or use cases
                    return "Congratulations! You have completed all the lessons."
        else:
            # No more lessons or use cases
            return "Congratulations! You have completed all the lessons."

    # Prepare the use case data for the template
    use_case_data = {
        "id": use_case.id,
        "lesson_id": use_case.lesson_id,
        "lesson_title": current_lesson["title"],
        "description": use_case.description,
        "questions": [
            {
                "id": question.id,
                "text": question.text,
                "options": [
                    {"id": option.id, "text": option.text}
                    for option in question.options
                ],
            }
            for question in use_case.questions
        ],
    }

    return render_template(
        "practice.html", use_case=use_case_data, is_similar_use_case=is_similar_use_case,
        total_use_cases=total_use_cases, correct_use_cases=correct_use_cases
    )

def get_lessons_use_case_count(lesson_id):
    return (db.session.query(UseCases)
        .filter(UseCases.lesson_id == lesson_id)
        .count()
    )

def get_users_correct_use_cases_per_lesson(lesson_id, user_id):
    return (db.session.query(UserAnswers)
        .filter(UserAnswers.lesson_id == lesson_id, UserAnswers.user_id == user_id, UserAnswers.is_correct)
        .count()
)


def find_similar_use_case(current_use_case_id, user_id):
    """
    Finds a use case similar to the current one based on shared risk factors.

    This function searches for a use case that shares risk factors with the current use case but has not yet been successfully completed by the user. This can help in recommending similar scenarios for further training or assessment.

    Args:
        current_use_case_id (int): The ID of the current use case.
        user_id (int): The ID of the user for whom similar use cases are being searched.

    Returns:
        UseCases | None: Returns a similar UseCase object if found, otherwise None.
    """
    current_use_case = UseCases.query.get(current_use_case_id)
    if not current_use_case:
        return None

    current_risk_factors = current_use_case.risk_factors

    # Query to find a similar use case based on risk factors
    similar_use_case = UseCases.query.filter(
        UseCases.id != current_use_case_id,
        UseCases.risk_factors.contains(current_risk_factors),
        ~UseCases.id.in_(
            db.session.query(UserAnswers.use_case_id)
            .filter(UserAnswers.user_id == user_id, UserAnswers.is_correct)
            .distinct()
        ),
    ).first()

    return similar_use_case


@app.route("/submit-answer", methods=["POST"])
def submit_answer():
    """
    Process answers submitted by the user for a use case, evaluate correctness, and respond appropriately.
    """
    data = request.get_json()
    app.logger.info(f"Received data: {data}")

    use_case_id = data.get("use_case_id")
    answers_data = data.get("answers")

    if not use_case_id or not answers_data:
        return jsonify({"error": "Missing use case ID or answers data"}), 400

    results = []
    has_mistake = False
    for answer in answers_data:
        question_id = answer.get("questionId")
        option_id = answer.get("answer")

        if not question_id or not option_id:
            return jsonify({"error": "Missing question ID or answer option ID"}), 400

        question = Questions.query.get(question_id)
        option = Options.query.filter_by(id=option_id, question_id=question_id).first()

        if not question or not option:
            return jsonify({"error": "Question or option not found"}), 404

        if question.use_case_id != int(use_case_id):
            return (
                jsonify(
                    {"error": "Question does not belong to the specified use case"}
                ),
                400,
            )

        is_correct = option.is_correct

        attempt = UserAnswers(
            user_id=current_user.id,
            use_case_id=int(use_case_id),
            question_id=int(question_id),
            option_id=int(option_id),
            is_correct=is_correct,
        )
        db.session.add(attempt)
        results.append({"questionId": question_id, "isCorrect": is_correct})

        if not is_correct:
            has_mistake = True

    db.session.commit()

    if has_mistake:
        # Find a similar use case based on risk factors
        similar_use_case = find_similar_use_case(use_case_id, current_user.id)
        if similar_use_case:
            # Store the similar use case ID in the session or temporary storage
            session["similar_use_case_id"] = similar_use_case.id

    next_use_case = get_next_use_case(use_case_id)
    if next_use_case:
        first_question = get_first_question_of_use_case(next_use_case.id)
        next_use_case_data = {
            "useCaseId": next_use_case.id,
            "description": next_use_case.description,
            "firstQuestion": prepare_first_question_data(first_question),
        }
        return (
            jsonify(
                {
                    "message": "Answer submitted successfully",
                    "isCorrect": is_correct,
                    "nextUseCase": next_use_case_data,
                }
            ),
            200,
        )
    else:
        return jsonify({"message": "No more use cases"}), 200


@app.route("/admin")
@login_required
def admin():
    """
    Display the admin page with a list of use cases created by the current logged-in user.

    Returns:
        Rendered template for the admin dashboard.
    """
    # Assuming 'current_user' is the logged-in user
    use_cases = UseCases.query.filter_by(created_by_user=current_user.id).all()
    return render_template("admin.html", use_cases=use_cases)


@app.route("/use-case/new", methods=["GET", "POST"])
@login_required
def new_use_case():
    """
    Create a new use case or display the form for creating a new use case, depending on the HTTP method.

    POST: Processes the form submission to create a new use case.
    GET: Displays the form to create a new use case.

    Returns:
        Redirect to admin page on successful creation or rendered creation form template.
    """
    if request.method == "POST":
        type = request.form["type"]
        description = request.form["description"]
        lesson_id = request.form.get("lesson_id")
        difficulty = request.form.get("difficulty")
        final_decision = request.form.get("final_decision")

        # Handle other fields similarly
        use_case = UseCases(
            type=type,
            description=description,
            lesson_id=lesson_id,
            difficulty=difficulty,
            final_decision=final_decision,
            created_by_user=current_user.id,
        )
        db.session.add(use_case)
        db.session.flush()  # Flush to assign an ID to the use case without committing

        # Now handle the question and answers
        question_text = request.form.get("question")
        question = Questions(text=question_text, use_case_id=use_case.id)
        db.session.add(question)
        db.session.flush()  # Flush to assign an ID to the question

        # Handle options creation
        for i in range(1, 5):  # Assuming 4 options based on the form
            option_text = request.form.get(f"option_{i}")
            is_correct = str(i) == request.form.get("correct_option")
            option = Options(
                text=option_text, question_id=question.id, is_correct=is_correct
            )
            db.session.add(option)

        db.session.commit()
        return redirect(url_for("admin"))

    # Assuming you have lists of lessons and difficulty levels to populate the form selections
    lessons = Lessons.query.all()
    difficulty_levels = DifficultyLevel.query.all()
    print(difficulty_levels)
    return render_template(
        "create_use_case.html", difficulty_levels=difficulty_levels, lessons=lessons
    )


@app.route("/use-case/<int:use_case_id>/edit", methods=["GET", "POST"])
@login_required
def edit_use_case(use_case_id):
    """
    Edit an existing use case or display the form for editing, depending on the HTTP method.

    POST: Processes the form submission to update the use case.
    GET: Displays the form pre-filled with the existing use case data.

    Args:
        use_case_id (int): The identifier of the use case to edit.

    Returns:
        Redirect to admin page on successful update or rendered edit form template.
    """
    use_case = UseCases.query.get_or_404(use_case_id)
    if request.method == "POST":
        # Update the use case fields based on the form data
        use_case.type = request.form["type"]
        use_case.description = request.form["description"]
        use_case.lesson_id = request.form.get("lesson_id")
        use_case.difficulty = request.form.get("difficulty")
        use_case.final_decision = request.form.get("final_decision")

        # Handle question and options updates
        question_text = request.form.get("question")
        question = Questions.query.filter_by(use_case_id=use_case.id).first()
        if question:
            question.text = question_text
        else:
            question = Questions(text=question_text, use_case_id=use_case.id)
            db.session.add(question)

        # Delete existing options
        Options.query.filter_by(question_id=question.id).delete()

        # Create new options
        for i in range(1, 5):
            option_text = request.form.get(f"option_{i}")
            is_correct = str(i) == request.form.get("correct_option")
            option = Options(
                text=option_text, question_id=question.id, is_correct=is_correct
            )
            db.session.add(option)

        db.session.commit()
        return redirect(url_for("admin"))

    # Retrieve the existing question and options for the use case
    question = Questions.query.filter_by(use_case_id=use_case.id).first()
    options = Options.query.filter_by(question_id=question.id).all() if question else []

    lessons = Lessons.query.all()
    difficulty_levels = DifficultyLevel.query.all()
    return render_template(
        "create_use_case.html",
        use_case=use_case,
        question=question,
        options=options,
        lessons=lessons,
        difficulty_levels=difficulty_levels,
    )


def get_first_question_of_use_case(use_case_id):
    """
    Retrieve the first question of a given use case by ID.

    Args:
        use_case_id (int): The identifier of the use case.

    Returns:
        The first question object or None if no question is associated with the use case.
    """
    return (
        Questions.query.filter_by(use_case_id=use_case_id)
        .order_by(Questions.id)
        .first()
    )


def record_attempt(
    user_id, use_case_id, question_id, user_answers, lesson_id, is_correct
):
    attempt = UserAnswers(
        user_id=user_id,
        use_case_id=use_case_id,
        question_id=question_id,
        option_id=",".join(user_answers),
        lesson_id=lesson_id,
        is_correct=is_correct,
    )
    db.session.add(attempt)
    db.session.commit()


def get_current_use_case(user_id, lesson_id):
    """
    Retrieves the first uncompleted use case in the given lesson for the specified user.

    Args:
        user_id (int): The identifier of the user.
        lesson_id (int): The identifier of the lesson.

    Returns:
        UseCases | None: The first uncompleted use case or None if all are completed.
    """
    # Get the IDs of use cases the user has completed in this lesson
    completed_use_cases = (
        db.session.query(UserAnswers.use_case_id)
        .filter(
            UserAnswers.user_id == user_id,
            UserAnswers.lesson_id == lesson_id,
            UserAnswers.is_correct == True,
        )
        .distinct()
        .subquery()
    )

    # Find the first uncompleted use case in the current lesson
    current_use_case = (
        UseCases.query.filter_by(lesson_id=lesson_id)
        .filter(~UseCases.id.in_(completed_use_cases))
        .order_by(UseCases.id)
        .first()
    )

    return current_use_case


def get_next_use_case(current_use_case_id):
    """
    Retrieve the next sequential use case following the current use case ID.

    Args:
        current_use_case_id (int): The identifier of the current use case.

    Returns:
        The next use case object or None if there is no subsequent use case.
    """
    # Check if there is a similar use case ID stored in the session
    similar_use_case_id = session.get("similar_use_case_id")
    if similar_use_case_id:
        # Retrieve the similar use case from the database
        similar_use_case = UseCases.query.get(similar_use_case_id)
        if similar_use_case:
            # Remove the similar use case ID from the session
            session.pop("similar_use_case_id", None)
            return similar_use_case

    current_use_case = UseCases.query.get(current_use_case_id)
    current_lesson_id = current_use_case.lesson_id

    # Check if the user has completed all the use cases in the current lesson
    completed_use_cases = UserAnswers.query.filter_by(
        user_id=current_user.id, is_correct=True
    ).all()
    completed_use_case_ids = [answer.use_case_id for answer in completed_use_cases]
    remaining_use_cases = (
        UseCases.query.filter(
            UseCases.lesson_id == current_lesson_id,
            UseCases.id > current_use_case_id,
            ~UseCases.id.in_(completed_use_case_ids),
        )
        .order_by(UseCases.id)
        .first()
    )

    if remaining_use_cases:
        return remaining_use_cases
    else:
        # Move on to the next lesson
        next_lesson = get_next_lesson(current_user.id)
        if next_lesson:
            # Retrieve the first use case of the next lesson
            next_use_case = (
                UseCases.query.filter_by(lesson_id=next_lesson["id"])
                .order_by(UseCases.id)
                .first()
            )
            return next_use_case
        else:
            return None


def prepare_first_question_data(first_question):
    """
    Prepare data for the first question of a use case to facilitate rendering or further processing.

    Args:
        question (Question): A question object.

    Returns:
        A dictionary containing the question ID, text, and options, or None if no question is provided.
    """
    if not first_question:
        return None  # or return an appropriate response indicating no questions are available

    # Prepare options data
    options_data = [
        {"id": option.id, "text": option.text} for option in first_question.options
    ]

    # Prepare and return question data
    question_data = {
        "questionId": first_question.id,
        "text": first_question.text,
        "options": options_data,
    }

    return question_data


def get_current_lesson(user_id):
    """Fetch the current lesson the user is on.

    Input:
    - user_id (int) -> user identifier

    Output:
    - lesson_id (int) -> lesson identifier
    """

    # Subquery to get the number of correct answers per lesson for the user
    correct_answers_subquery = (
        db.session.query(
            UserAnswers.lesson_id, func.count(UserAnswers.id).label("correct_count")
        )
        .filter(UserAnswers.user_id == user_id, UserAnswers.is_correct == True)
        .group_by(UserAnswers.lesson_id)
        .subquery()
    )

    # Subquery to get the total number of questions per lesson
    total_questions_subquery = (
        db.session.query(
            UseCases.lesson_id, func.count(Questions.id).label("total_questions")
        )
        .join(Questions, UseCases.id == Questions.use_case_id)
        .group_by(UseCases.lesson_id)
        .subquery()
    )

    # Join the two subqueries to find lessons where the number of correct answers equals the total number of questions
    completed_lessons_subquery = (
        db.session.query(total_questions_subquery.c.lesson_id)
        .join(
            correct_answers_subquery,
            correct_answers_subquery.c.lesson_id
            == total_questions_subquery.c.lesson_id,
        )
        .filter(
            correct_answers_subquery.c.correct_count
            == total_questions_subquery.c.total_questions
        )
        .subquery()
    )

    # Find the first lesson that the user hasn't completed correctly
    current_lesson = (
        db.session.query(Lessons)
        .outerjoin(
            completed_lessons_subquery,
            Lessons.id == completed_lessons_subquery.c.lesson_id,
        )
        .filter(completed_lessons_subquery.c.lesson_id == None)
        .order_by(Lessons.id)
        .first()
    )

    if current_lesson:
        print(current_lesson)
        return {"id": current_lesson.id, "title": current_lesson.title}

    return None


def update_lesson_progress(user_id, lesson_id, progress, score=None):
    interaction = UserLessonInteraction.query.filter_by(
        user_id=user_id, lesson_id=lesson_id
    ).first()
    if interaction:
        interaction.progress = progress
        interaction.last_accessed = datetime.utcnow()
        if progress >= 100:
            interaction.completed = True
            interaction.completion_date = datetime.utcnow()
            interaction.score = score
    else:
        interaction = UserLessonInteraction(
            user_id=user_id,
            lesson_id=lesson_id,
            progress=progress,
            last_accessed=datetime.utcnow(),
            completed=progress >= 100,
            completion_date=datetime.utcnow() if progress >= 100 else None,
            score=score if progress >= 100 else None,
        )
        db.session.add(interaction)
    db.session.commit()

    return interaction


def get_next_lesson(user_id: int) -> Dict[str, Any]:
    """
    Retrieves the next lesson for a user based on their progress and difficulty level.
    """
    last_interaction = (
        UserLessonInteraction.query.filter_by(user_id=user_id)
        .order_by(UserLessonInteraction.last_accessed.desc())
        .first()
    )
    print(last_interaction)

    if last_interaction and last_interaction.completed:
        next_lesson = (
            Lessons.query.filter(Lessons.id > last_interaction.lesson_id)
            .order_by(Lessons.id)
            .first()
        )
        print(next_lesson)
    else:
        next_lesson = (
            Lessons.query.filter_by(id=last_interaction.lesson_id).first()
            if last_interaction
            else Lessons.query.first()
        )

    if next_lesson:
        # Retrieve the associated use cases for the next lesson
        use_cases = UseCases.query.filter_by(lesson_id=next_lesson.id).all()
        lesson_data = {
            "id": next_lesson.id,
            "title": next_lesson.title,
            "use_cases": [
                {
                    "id": use_case.id,
                    "description": use_case.description,
                    # Include other relevant use case data
                }
                for use_case in use_cases
            ],
        }

        return lesson_data
    return None
