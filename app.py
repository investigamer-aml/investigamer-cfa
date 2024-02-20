from enum import Enum
from typing import Optional, Dict, Any
from pydantic import BaseModel, EmailStr, field_validator, constr, conint

from flask import Flask, request, session, jsonify, render_template, redirect, url_for, jsonify
from flask_login import login_user, current_user, login_required, logout_user, UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask('INVESTIGAMER')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://data_admin:investigamer@localhost/ig_data_admin'
app.config['SECRET_KEY'] = '78f78214cd0360e847034d3bda9d117f'
# app.config['SQLALCHEMY_ECHO'] = True

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

class DifficultyLevel(str, Enum):
    easy = "Easy"
    medium = "Medium"
    hard = "Hard"

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)
    use_case_difficulty = db.Column(db.String(128), nullable=False)
    score = db.Column(db.Float, nullable = False)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

class LearningPath(BaseModel):
    id: conint(gt=0)
    user_id: conint(gt=0)
    name: constr(min_length=1)
    description: Optional[str] = None

class Lesson(BaseModel):
    id: conint(gt=0)
    title: constr(min_length=1)

class UseCases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    difficulty = db.Column(db.String, db.ForeignKey('difficulty_level.level'), nullable=False)  # Adjust as needed
    multiple_risks = db.Column(db.Boolean, nullable=False)
    correct_answer = db.Column(db.String, nullable=False)
    final_decision = db.Column(db.String, nullable=False)
    risk_factor_matrix_id = db.Column(db.Integer, db.ForeignKey('risk_factor_matrix.id'), nullable=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    questions = db.relationship('Questions', backref='use_cases', lazy=True)

class RiskFactorMatrix(BaseModel):
    id: conint(gt=0)
    factor: constr(min_length=1)
    score: conint(ge=0, le=100)  # Score is between 0 and 100
    use_case_id: conint(gt=0)

class UserAnswers(db.Model):
    __tablename__ = 'user_answers'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    use_case_id = db.Column(db.Integer, db.ForeignKey('use_cases.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('options.id'), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)

    user = db.relationship('Users', backref=db.backref('user_answers', lazy=True))
    use_case = db.relationship('UseCases', backref=db.backref('use_case_answers', lazy=True))
    question = db.relationship('Questions', backref=db.backref('question_answers', lazy=True))
    option = db.relationship('Options', backref=db.backref('option_answers', lazy=True))


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    use_case_id = db.Column(db.Integer, db.ForeignKey('use_cases.id'), nullable=False)
    text = db.Column(db.String, nullable=False)
    options = db.relationship('Options', backref='questions', lazy=True)

class Options(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    text = db.Column(db.String, nullable=False)
    is_correct = db.Column(db.Boolean, default=False, nullable=False)


##### REGISTRATION #####
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if user already exists
    user_exists = Users.query.filter((Users.email == email) | (Users.username == username)).first()
    if user_exists:
        return jsonify({'error': 'User already exists'}), 400

    # Create new user
    new_user = Users(username=username, email=email)
    new_user.set_password(password)  # Hash password
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

    username = request.form.get('username')
    password = request.form.get('password')

    # Authenticate user
    user = Users.query.filter_by(username=username).first()
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
    # Retrieve the first question for the lesson_id
    use_case = UseCases.query.order_by(UseCases.id).filter_by(lesson_id=1).first() #fix it to Easy for now
    if use_case:
        return render_template('practice.html', use_case=use_case)
    else:
        return "Lesson not found", 404

@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    app.logger.info(f"Received data: {data}")

    # Extract the use_case_id from the JSON payload
    use_case_id = data.get('use_case_id')
    answers_data = data.get('answers')

    if not use_case_id or not answers_data:
        return jsonify({'error': 'Missing use case ID or answers data'}), 400

    results = []
    for answer in answers_data:
        question_id = answer.get('questionId')
        option_id = answer.get('answer')

        if not question_id or not option_id:
            return jsonify({'error': 'Missing question ID or answer option ID'}), 400

        # Fetch the question and option to verify the submission
        question = Questions.query.get(question_id)
        option = Options.query.filter_by(id=option_id, question_id=question_id).first()

        if not question or not option:
            return jsonify({'error': 'Question or option not found'}), 404

        if question.use_case_id != int(use_case_id):  # Ensure correct use case
            return jsonify({'error': 'Question does not belong to the specified use case'}), 400

        # Determine if the submitted option is correct
        is_correct = option.is_correct

        # Record the attempt
        attempt = UserAnswers(
            user_id=current_user.id,
            use_case_id=int(use_case_id),
            question_id=int(question_id),
            option_id=int(option_id),
            is_correct=is_correct
        )
        db.session.add(attempt)
        results.append({'questionId': question_id, 'isCorrect': is_correct})

    db.session.commit()

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


    # return jsonify({'message': 'Answers submitted successfully', 'results': results}), 200


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

def render_question(question):
    # Render the question page with options
    # This will include question text and multiple-choice options
    pass

def evaluate_answer(user_id: int, question_id: int, given_answer: str) -> bool:
    """
    Evaluates a given answer against the correct answer in the database.
    Returns True if the answer is correct, False otherwise.
    """
    # Placeholder for actual database query to get the correct answer
    correct_answer = "A"
    is_correct = given_answer == correct_answer
    # Here we would also update the user's progress in the database
    return is_correct

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

if __name__ == '__main__':
    app.run(debug=True)