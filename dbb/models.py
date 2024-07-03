""" DB models for the investigamer app
"""
import json
from datetime import datetime, timezone
from typing import List, Optional

from flask_login import UserMixin
from sqlalchemy import JSON, Boolean, DateTime, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import TEXT, TypeDecorator
from werkzeug.security import check_password_hash, generate_password_hash

from app import db


class JSONEncodedDict(TypeDecorator):
    impl = TEXT

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return json.loads(value)


class DifficultyLevel(db.Model):
    """Represents the difficulty level of a use case."""

    __tablename__ = "difficulty_level"

    id: Mapped[int] = mapped_column(primary_key=True)
    level: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    def __repr__(self) -> str:
        """
        Returns a string representation of the DifficultyLevel instance, including its level.

        Returns:
            str: A string representation of the DifficultyLevel instance.
        """
        return f"<DifficultyLevel {self.level}>"


class Users(UserMixin, db.Model):
    """Represents a User in the system."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    use_case_difficulty: Mapped[str] = mapped_column(String(128), nullable=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"), nullable=True)
    score: Mapped[float] = mapped_column(Float, nullable=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    lesson: Mapped["Lessons"] = relationship(back_populates="users")
    user_answers: Mapped[List["UserAnswers"]] = relationship(back_populates="user")
    lesson_interactions: Mapped[List["UserLessonInteraction"]] = relationship(
        back_populates="user"
    )

    def get_id(self):
        """
        Get the unique identifier for the current user.

        This method overrides the default get_id method provided by UserMixin to return the user's ID as a string.

        Returns:
            str: The unique identifier of the user as a string.
        """
        return str(self.id)

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


class Lessons(db.Model):
    """Represents an educational lesson."""

    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)

    users: Mapped[List["Users"]] = relationship(back_populates="lesson")
    use_cases: Mapped[List["UseCases"]] = relationship(back_populates="lesson")
    user_interactions: Mapped[List["UserLessonInteraction"]] = relationship(
        back_populates="lesson"
    )


class UseCases(db.Model):
    """Represents a use case within the system."""

    __tablename__ = "use_cases"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    difficulty_id: Mapped[int] = mapped_column(
        ForeignKey("difficulty_level.id"), nullable=False
    )
    risk_factors: Mapped[Optional[dict]] = mapped_column(JSON)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"), nullable=False)
    created_by_user: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    lesson: Mapped["Lessons"] = relationship(back_populates="use_cases")
    questions: Mapped[List["Questions"]] = relationship(back_populates="use_case")
    news_articles: Mapped[List["NewsArticle"]] = relationship(back_populates="use_case")
    use_case_answers: Mapped[List["UserAnswers"]] = relationship(
        back_populates="use_case"
    )

    def __repr__(self) -> str:
        """
        Returns a string representation of the UseCase instance, including its description.

        Returns:
            str: A string representation of the UseCase instance.
        """
        return f"<UseCase {self.description}>"


class UserAnswers(db.Model):
    """Stores responses from users to specific questions in specific use cases."""

    __tablename__ = "user_answers"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    use_case_id: Mapped[int] = mapped_column(ForeignKey("use_cases.id"), nullable=False)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id"), nullable=False)
    option_id: Mapped[int] = mapped_column(ForeignKey("options.id"), nullable=False)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"), nullable=False)
    is_correct: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, nullable=False
    )

    user: Mapped["Users"] = relationship(back_populates="user_answers")
    use_case: Mapped["UseCases"] = relationship(back_populates="use_case_answers")
    question: Mapped["Questions"] = relationship(back_populates="question_answers")
    option: Mapped["Options"] = relationship(back_populates="option_answers")


class Questions(db.Model):
    """Represents a question associated with a use case."""

    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    use_case_id: Mapped[int] = mapped_column(ForeignKey("use_cases.id"), nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)

    use_case: Mapped["UseCases"] = relationship(back_populates="questions")
    options: Mapped[List["Options"]] = relationship(back_populates="question")
    question_answers: Mapped[List["UserAnswers"]] = relationship(
        back_populates="question"
    )


class Options(db.Model):
    """Represents an answer option for a particular question."""

    __tablename__ = "options"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id"), nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)
    is_correct: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    question: Mapped["Questions"] = relationship(back_populates="options")
    option_answers: Mapped[List["UserAnswers"]] = relationship(back_populates="option")


class UserLessonInteraction(db.Model):
    """Represents an interaction between a user and a lesson."""

    __tablename__ = "user_lesson_interactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    completion_date: Mapped[Optional[datetime]] = mapped_column(DateTime)
    score: Mapped[Optional[float]] = mapped_column(Float)
    last_accessed: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["Users"] = relationship(back_populates="lesson_interactions")
    lesson: Mapped["Lessons"] = relationship(back_populates="user_interactions")

    def __repr__(self) -> str:
        """
        Returns a string representation of the UserLessonInteraction instance, including its user_id, lesson_id, and completion status.

        Returns:
            str: A string representation of the UserLessonInteraction instance.
        """
        return f"<UserLessonInteraction(user_id={self.user_id}, lesson_id={self.lesson_id}, completed={self.completed})>"


class NewsArticle(db.Model):
    """Represents a news article generated from a use case scenario."""

    __tablename__ = "news_articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String, nullable=False)
    use_case_id: Mapped[int] = mapped_column(ForeignKey("use_cases.id"), nullable=False)

    use_case: Mapped["UseCases"] = relationship(back_populates="news_articles")
