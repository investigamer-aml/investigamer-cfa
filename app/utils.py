""" Module to store all small utility helper functions
"""
from typing import Any, Dict, Optional

from flask import current_app as app
from markdown import markdown
from markupsafe import Markup
from sqlalchemy import select
from werkzeug.security import generate_password_hash

from app import db
from dbb.models import (Lessons, Questions, UseCases, UserAnswers,
                        UserLessonInteraction)


def set_password(password):
    """Generate a hash of a user password to save into the db"""
    return generate_password_hash(password)


# Flatten the JSON objects for easier comparison
def flatten_json(y):
    """Extract all objects from a json and flatten it out"""
    out = {}

    def flatten(x, name=""):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + ".")
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def json_contains(json_obj, query, threshold=0.75):
    """Check if json_obj contains at least the threshold percentage of key-value pairs in query."""

    flat_json_obj = flatten_json(json_obj)
    flat_query = flatten_json(query)

    total_keys = len(flat_query)
    matching_keys = sum(
        1
        for key in flat_query
        if key in flat_json_obj and flat_json_obj[key] == flat_query[key]
    )

    similarity = matching_keys / total_keys if total_keys > 0 else 0
    formatted_similarity = f"{similarity:.2%}"
    app.logger.info(f"Similarity = {formatted_similarity}")

    return similarity >= threshold


def find_similar_use_case(current_use_case_id, user_id, lesson_id):
    """
    Finds a use case similar to the current one based on shared risk factors.

    This function searches for a use case that shares risk factors with the current use case but has not yet been successfully completed by the user. This can help in recommending similar scenarios for further training or assessment.

    Args:
        current_use_case_id (int): The ID of the current use case.
        user_id (int): The ID of the user for whom similar use cases are being searched.

    Returns:
        UseCases | None: Returns a similar UseCase object if found, otherwise None.
    """
    current_use_case = db.session.get(UseCases, int(current_use_case_id))
    if not current_use_case:
        return None

    app.logger.info(f"Current Case {current_use_case.risk_factors}")

    current_risk_factors = current_use_case.risk_factors
    # current_risk_factors = json.loads(current_risk_factors)

    # Query to find a similar use case based on risk factors
    similar_use_cases = UseCases.query.filter(
        UseCases.lesson_id == lesson_id,
        UseCases.id != current_use_case_id,
        ~UseCases.id.in_(
            db.session.query(UserAnswers.use_case_id)
            .filter(UserAnswers.user_id == user_id, UserAnswers.is_correct)
            .distinct()
        ),
    ).all()

    for use_case in similar_use_cases:
        risk_factors = use_case.risk_factors
        if json_contains(risk_factors, current_risk_factors):
            return use_case

    return None


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


def get_next_use_case(current_use_case_id, user_id, lesson_id):
    """
    Retrieves the next use case for a user, considering similar cases and lesson progression.

    Args:
        current_use_case_id (int): The ID of the current use case.
        user_id (int): The ID of the user.
        lesson_id (int): The ID of the current lesson.

    Returns:
        UseCases | None: The next use case object or None if there are no more use cases.
    """
    current_use_case = db.session.get(UseCases, int(current_use_case_id))
    if not current_use_case:
        return None

    # Check for a similar use case first
    similar_use_case = find_similar_use_case(current_use_case_id, user_id, lesson_id)
    if similar_use_case:
        return similar_use_case

    # Get completed use cases for this user in this lesson
    completed_use_cases = (
        select(UserAnswers.use_case_id)
        .where(
            UserAnswers.user_id == user_id,
            UserAnswers.lesson_id == lesson_id,
            UserAnswers.is_correct == True,
        )
        .distinct()
    )

    # Find the next uncompleted use case in the current lesson
    next_use_case = (
        UseCases.query.filter(
            UseCases.lesson_id == lesson_id,
            UseCases.id > current_use_case_id,
            ~UseCases.id.in_(completed_use_cases),
        )
        .order_by(UseCases.id)
        .first()
    )

    if next_use_case:
        return next_use_case

    # If no next use case in the current lesson, check for the next lesson
    next_lesson = (
        Lessons.query.filter(Lessons.id > lesson_id).order_by(Lessons.id).first()
    )
    if next_lesson:
        # Find the first uncompleted use case in the next lesson
        first_use_case_next_lesson = (
            UseCases.query.filter(
                UseCases.lesson_id == next_lesson.id,
                ~UseCases.id.in_(
                    db.session.query(UserAnswers.use_case_id)
                    .filter(UserAnswers.user_id == user_id, UserAnswers.is_correct)
                    .distinct()
                ),
            )
            .order_by(UseCases.id)
            .first()
        )
        return first_use_case_next_lesson

    return None  # No more use cases available


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


def render_markdown(content):
    """Convert Markdown formatted text to HTML"""
    html = markdown(content)
    return Markup(html)


def get_lessons_use_case_count(lesson_id):
    """Get the total number of cases in a lesson"""
    return db.session.query(UseCases).filter(UseCases.lesson_id == lesson_id).count()


def get_users_correct_use_cases_per_lesson(lesson_id, user_id):
    """Check how many correct use cases a user has submitted within a lesson"""
    return (
        db.session.query(UserAnswers)
        .filter(
            UserAnswers.lesson_id == lesson_id,
            UserAnswers.user_id == user_id,
            UserAnswers.is_correct,
        )
        .count()
    )
