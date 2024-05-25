from datetime import datetime
from enum import Enum

from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import JSONB
from werkzeug.security import check_password_hash, generate_password_hash

from app import db


class DifficultyLevel(db.Model):
    """
    Represents the difficulty level of a use case, allowing for the categorization and appropriate assignment of use cases to users based on their skill level.
    """

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        """Print itself"""
        return f"<DifficultyLevel {self.level}>"


class Users(UserMixin, db.Model):
    """
    Represents a User in the system, capable of logging in and interacting with the application.
    Stores information such as username, email, password hash, and administrative status.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)
    use_case_difficulty = db.Column(db.String(128), nullable=False)
    score = db.Column(db.Float, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)  # Add this line

    def set_password(self, password):
        """
        Sets the password for the current user, storing a hash of it rather than the plain text.

        Args:
            password (str): The password to hash and store.
        """
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        """
        Checks if the provided password matches the stored hash for this user.

        Args:
            password (str): The password to check against the stored hash.

        Returns:
            bool: True if the password matches the hash, False otherwise.
        """
        return check_password_hash(self.hashed_password, password)


# class LearningPath(BaseModel):
#     id: conint(gt=0)
#     user_id: conint(gt=0)
#     name: constr(min_length=1)
#     description: Optional[str] = None


class Lessons(db.Model):
    """
    Represents an educational lesson which may contain multiple use cases. Lessons provide structured learning paths.
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)


class UseCases(db.Model):
    """
    Represents a use case within the system which encompasses a scenario that a user can practice or be tested on.
    Includes relationships to questions and other related data.
    """

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    difficulty = db.Column(
        db.String, db.ForeignKey("difficulty_level.level"), nullable=False
    )  # Adjust as needed
    multiple_risks = db.Column(db.Boolean, nullable=False)
    final_decision = db.Column(db.String, nullable=False)
    risk_factors = db.Column(JSONB)  # Use JSONB for the risk factors
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=False)
    questions = db.relationship("Questions", backref="use_cases", lazy=True)
    created_by_user = db.Column(
        db.String, db.ForeignKey("users.id"), nullable=False
    )  # Adjust as needed

    def __repr__(self):
        """Print itself"""
        return "<UseCase %r>" % self.title


# class RiskFactorMatrix(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     factor = db.Column(db.String, nullable=False)
#     score = db.Column(db.Float, nullable=False)
#     use_case_id = db.Column(db.Integer, db.ForeignKey("use_cases.id"), nullable=False)


class UserAnswers(db.Model):
    """
    Stores responses from users to specific questions in specific use cases, recording whether the answers were correct.
    """

    __tablename__ = "user_answers"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    use_case_id = db.Column(db.Integer, db.ForeignKey("use_cases.id"), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey("options.id"), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship("Users", backref=db.backref("user_answers", lazy=True))
    use_case = db.relationship(
        "UseCases", backref=db.backref("use_case_answers", lazy=True)
    )
    question = db.relationship(
        "Questions", backref=db.backref("question_answers", lazy=True)
    )
    option = db.relationship("Options", backref=db.backref("option_answers", lazy=True))


class Questions(db.Model):
    """
    Represents a question associated with a use case. Questions are linked to use cases and have multiple possible answers.
    """

    id = db.Column(db.Integer, primary_key=True)
    use_case_id = db.Column(db.Integer, db.ForeignKey("use_cases.id"), nullable=False)
    text = db.Column(db.String, nullable=False)
    options = db.relationship("Options", backref="questions", lazy=True)


class Options(db.Model):
    """
    Represents an answer option for a particular question. Each option knows whether it is the correct answer for its question.
    """

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    text = db.Column(db.String, nullable=False)
    is_correct = db.Column(db.Boolean, default=False, nullable=False)
