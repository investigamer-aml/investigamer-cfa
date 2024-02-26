from app import db
from flask_login import UserMixin
from enum import Enum
from werkzeug.security import generate_password_hash, check_password_hash


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
    is_admin = db.Column(db.Boolean, default=False, nullable=False)  # Add this line

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

# class LearningPath(BaseModel):
#     id: conint(gt=0)
#     user_id: conint(gt=0)
#     name: constr(min_length=1)
#     description: Optional[str] = None

# class Lesson(BaseModel):
#     id: conint(gt=0)
#     title: constr(min_length=1)

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

# class RiskFactorMatrix(BaseModel):
#     id: conint(gt=0)
#     factor: constr(min_length=1)
#     score: conint(ge=0, le=100)  # Score is between 0 and 100
#     use_case_id: conint(gt=0)

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