from app import db
from typing import Optional, Dict, Any
from flask import current_app as app
from flask import Flask, request, session, jsonify, render_template, redirect, url_for, jsonify
from flask_login import login_user, current_user, login_required, logout_user, UserMixin, LoginManager
from .models import Users, UseCases, Questions, UserAnswers, Options, Lessons, DifficultyLevel
import markdown
from datetime import datetime

login_manager = LoginManager()
login_manager.init_app(app)


##### REGISTRATION #####
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    is_admin = 'is_admin' in request.form

    # Check if user already exists
    user_exists = Users.query.filter((Users.email == email) | (Users.username == username)).first()
    if user_exists:
        return jsonify({'error': 'User already exists'}), 400

    # Create new user
    new_user = Users(username=username, email=email, is_admin=is_admin)
    new_user.set_password(password)  # Hash password
    new_user.is_admin = is_admin  # Setting the is_admin flag based on checkbox
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login'))  # Redirect to the login page


@app.route('/register', methods=['GET'])
def show_register():
    return render_template('register.html')

####### LOGIN #######
@app.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))  # Redirect to the homepage

    login_input = request.form.get('login_input')  # Assuming you change the form to have 'login_input' instead of 'username'
    password = request.form.get('password')

    # Attempt to authenticate first by username, then by email
    user = Users.query.filter((Users.username == login_input) | (Users.email == login_input)).first()

    if user and user.check_password(password):
        login_user(user)
        return redirect(url_for('home'))  # Redirect to the homepage
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/login', methods=['GET'])
def show_login():
    return render_template('login.html')

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route('/profile')
@login_required
def profile():
    # Assuming you have a user object in the session
    return render_template('profile.html', user=current_user)

@app.route('/')
def home():
    return render_template('index.html')

# Define your models based on the provided schema
# @app.route('/practice/<int:lesson_id>')
@app.route('/practice')
def start_lesson():
    use_case = UseCases.query.order_by(UseCases.id).filter_by(lesson_id=1).first()
    use_case.description = markdown.markdown(use_case.description)
    if use_case:
        use_case_data = {
            'id': use_case.id,
            'description': use_case.description,
            'questions': [
                {
                    'id': question.id,
                    'text': question.text,
                    'options': [
                        {
                            'id': option.id,
                            'text': option.text
                        } for option in question.options
                    ]
                } for question in use_case.questions
            ]
        }
        return render_template('practice.html', use_case=use_case_data)
    else:
        return "Lesson not found", 404

def find_similar_use_case(current_use_case_id, user_id):
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
            .filter(UserAnswers.user_id == user_id, UserAnswers.is_correct == True)
            .distinct()
        )
    ).first()

    return similar_use_case

@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    app.logger.info(f"Received data: {data}")

    use_case_id = data.get('use_case_id')
    answers_data = data.get('answers')

    if not use_case_id or not answers_data:
        return jsonify({'error': 'Missing use case ID or answers data'}), 400

    results = []
    has_mistake = False
    for answer in answers_data:
        question_id = answer.get('questionId')
        option_id = answer.get('answer')

        if not question_id or not option_id:
            return jsonify({'error': 'Missing question ID or answer option ID'}), 400

        question = Questions.query.get(question_id)
        option = Options.query.filter_by(id=option_id, question_id=question_id).first()

        if not question or not option:
            return jsonify({'error': 'Question or option not found'}), 404

        if question.use_case_id != int(use_case_id):
            return jsonify({'error': 'Question does not belong to the specified use case'}), 400

        is_correct = option.is_correct

        attempt = UserAnswers(
            user_id=current_user.id,
            use_case_id=int(use_case_id),
            question_id=int(question_id),
            option_id=int(option_id),
            is_correct=is_correct
        )
        db.session.add(attempt)
        results.append({'questionId': question_id, 'isCorrect': is_correct})

        if not is_correct:
            has_mistake = True

    db.session.commit()

    if has_mistake:
        # Find a similar use case based on risk factors
        similar_use_case = find_similar_use_case(use_case_id, current_user.id)
        if similar_use_case:
            # Store the similar use case ID in the session or temporary storage
            session['similar_use_case_id'] = similar_use_case.id

    next_use_case = get_next_use_case(use_case_id)
    if next_use_case:
        first_question = get_first_question_of_use_case(next_use_case.id)
        next_use_case_data = {
            "useCaseId": next_use_case.id,
            "description": next_use_case.description,
            "firstQuestion": prepare_first_question_data(first_question)
        }
        return jsonify({'message': 'Answer submitted successfully', 'isCorrect': is_correct, 'nextUseCase': next_use_case_data}), 200
    else:
        return jsonify({'message': 'No more use cases'}), 200

@app.route('/admin')
@login_required
def admin():
    # Assuming 'current_user' is the logged-in user
    use_cases = UseCases.query.filter_by(created_by_user=current_user.id).all()
    return render_template('admin.html', use_cases=use_cases)

@app.route('/use-case/new', methods=['GET', 'POST'])
@login_required
def new_use_case():
    if request.method == 'POST':
        type = request.form['type']
        description = request.form['description']
        lesson_id = request.form.get('lesson_id')
        difficulty = request.form.get('difficulty')
        final_decision = request.form.get('final_decision')

        # Handle other fields similarly
        use_case = UseCases(
            type=type,
            description=description,
            lesson_id=lesson_id,
            difficulty=difficulty,
            final_decision=final_decision,
            created_by_user=current_user.id
        )
        db.session.add(use_case)
        db.session.flush()  # Flush to assign an ID to the use case without committing

                # Now handle the question and answers
        question_text = request.form.get('question')
        question = Questions(text=question_text, use_case_id=use_case.id)
        db.session.add(question)
        db.session.flush()  # Flush to assign an ID to the question

        # Handle options creation
        for i in range(1, 5):  # Assuming 4 options based on the form
            option_text = request.form.get(f'option_{i}')
            is_correct = (str(i) == request.form.get('correct_option'))
            option = Options(text=option_text, question_id=question.id, is_correct=is_correct)
            db.session.add(option)

        db.session.commit()
        return redirect(url_for('admin'))

    # Assuming you have lists of lessons and difficulty levels to populate the form selections
    lessons = Lessons.query.all()
    difficulty_levels = DifficultyLevel.query.all()
    print(difficulty_levels)
    return render_template('create_use_case.html', difficulty_levels=difficulty_levels, lessons=lessons)

@app.route('/use-case/<int:use_case_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_use_case(use_case_id):
    use_case = UseCases.query.get_or_404(use_case_id)
    if request.method == 'POST':
        # Update the use case fields based on the form data
        use_case.type = request.form['type']
        use_case.description = request.form['description']
        use_case.lesson_id = request.form.get('lesson_id')
        use_case.difficulty = request.form.get('difficulty')
        use_case.final_decision = request.form.get('final_decision')

        # Handle question and options updates
        question_text = request.form.get('question')
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
            option_text = request.form.get(f'option_{i}')
            is_correct = (str(i) == request.form.get('correct_option'))
            option = Options(text=option_text, question_id=question.id, is_correct=is_correct)
            db.session.add(option)

        db.session.commit()
        return redirect(url_for('admin'))

    # Retrieve the existing question and options for the use case
    question = Questions.query.filter_by(use_case_id=use_case.id).first()
    options = Options.query.filter_by(question_id=question.id).all() if question else []

    lessons = Lessons.query.all()
    difficulty_levels = DifficultyLevel.query.all()
    return render_template('create_use_case.html', use_case=use_case, question=question, options=options, lessons=lessons, difficulty_levels=difficulty_levels)

def get_first_question_of_use_case(use_case_id):
    return Questions.query.filter_by(use_case_id=use_case_id).order_by(Questions.id).first()

def prepare_first_question_data(question):
    if not question:
        return None  # or an appropriate placeholder

    return {
        "questionId": question.id,
        "text": question.text,
        "options": [
            {"id": option.id, "text": option.text} for option in question.options
        ]
    }

def record_attempt(user_id, question_id, user_answers, correct):
    attempt = UserAnswers(user_id=user_id, use_case_id=question_id, option_id=','.join(user_answers), is_correct=correct)
    db.session.add(attempt)
    db.session.commit()

def find_similar_question(question_id, user_id, lesson_id):
    # SQL query to find a question with a similar difficulty level
    # within the same lesson that the user hasn't answered correctly.
    similar_questions_query = """
        select u.*
        from   use_cases u
        where  u.difficulty in (
                select difficulty
                from   use_cases
            )
        and  u.id not in (
                select use_case_id
                from   user_answers
                where  user_answers.is_correct = true
            )
        order by random() desc
        limit 1;
    """
    result = db.session.execute(similar_questions_query, (lesson_id, question_id, user_id))
    return result.fetchone()  # Assuming this function fetches the next similar question

def get_next_use_case(current_use_case_id):
    # Assuming use cases are ordered or have an identifier to determine sequence
    next_use_case = UseCases.query.filter(UseCases.id > current_use_case_id).order_by(UseCases.id).first()

    if not next_use_case:
        return None

    # Assuming the first question is simply the first in order by ID
    first_question = Questions.query.filter_by(use_case_id=next_use_case.id).order_by(Questions.id).first()
    app.logger.info(f"First question of next use case: {first_question}")
    first_question_data = prepare_first_question_data(first_question)

    # Prepare the rest of the next use case data as before, including the first question data
    next_use_case_data = {
        "useCaseId": next_use_case.id,
        "description": next_use_case.description,
        "firstQuestion": first_question_data  # Include first question data
    }

    return next_use_case

def prepare_first_question_data(first_question):
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
        "options": options_data
    }

    return question_data


def get_next_lesson(user_id: int) -> Dict[str, Any]:
    """
    Retrieves the next lesson for a user based on their progress and difficulty level.
    """
    # Placeholder for actual database query
    lesson = {
        "id": 1,
        "title": "Introduction to Anti Money Laundering",
        "content": "Understanding the basics of AML...",
        "questions": [
            {"id": 1, "question": "What is Money Laundering?", "options": ["A", "B", "C"], "answer": "A"}
        ]
    }
    return lesson