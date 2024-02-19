from enum import Enum
from typing import Optional, Dict, Any
from pydantic import BaseModel, EmailStr, field_validator, constr, conint

from flask import Flask, render_template
from flask import Flask, request, session, jsonify, render_template, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user, UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask('INVESTIGAMER')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://data_admin:investigamer@localhost/ig_data_admin'
app.config['SECRET_KEY'] = '78f78214cd0360e847034d3bda9d117f'

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

class RiskFactorMatrix(BaseModel):
    id: conint(gt=0)
    factor: constr(min_length=1)
    score: conint(ge=0, le=100)  # Score is between 0 and 100
    use_case_id: conint(gt=0)

class UserAnswer(BaseModel):
    id: conint(gt=0)
    user_id: conint(gt=0)
    use_case_id: conint(gt=0)
    answer_given: constr(min_length=1)
    is_correct: bool

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    use_case_id = db.Column(db.Integer, db.ForeignKey('use_case.id'), nullable=False)
    text = db.Column(db.String, nullable=False)
    options = db.relationship('Option', backref='question', lazy=True)

class Options(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
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
# def home():
#     first_use_case = UseCases.query.first()  # Assuming UseCase is an ORM model
#     if first_use_case:
#         # Render your index page with the first use case details
#         return render_template('index.html', use_case=first_use_case)
#     else:
#         return "No use cases found", 404
def home():
    return render_template('index.html')

# Define your models based on the provided schema
# @app.route('/practice/<int:lesson_id>')
@app.route('/practice')
def start_lesson():
    # Retrieve the first question for the lesson_id
    use_case = UseCases.query.filter_by(id=1).first() #fix it to Easy for now
    if use_case:
        return render_template('practice.html', use_case=use_case)
    else:
        return "Lesson not found", 404

@app.route('/submit-answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    question_id = data['question_id']
    user_answers = data['answers']
    question = UseCases.query.get(question_id)

    if not question:
        return "Question not found", 404

    # Assume answers are sent as a list of IDs and we check if all are in the question.correct_answer
    correct = all(answer in question.correct_answer.split(',') for answer in user_answers)
    user_id = 1  # This should be the session user ID
    record_attempt(user_id, question_id, user_answers, correct)

    if correct:
        next_question = get_next_question(question_id)
        return jsonify({'question': next_question})
    else:
        return jsonify({'question': question_id})  # Send back the same question ID

def get_first_question(lesson_id):
    # SQL query to get the first question of the lesson
    pass

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
    attempt = UserAnswer(user_id=user_id, use_case_id=question_id, answer_given=','.join(user_answers), is_correct=correct)
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

def get_next_question(current_question_id):
    current_question = UseCases.query.get(current_question_id)
    next_question = UseCases.query.filter(UseCases.id > current_question_id, UseCases.type == current_question.type).order_by(UseCases.id).first()
    return next_question.id if next_question else None

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