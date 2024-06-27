""" Module to handle endpoints for use case related stuff
"""

from flask import Blueprint
from flask import current_app as app
from flask import jsonify, request, session
from flask_login import current_user, login_required

from app import db
from dbb.models import Options, Questions, UserAnswers

from .utils import (find_similar_use_case, get_first_question_of_use_case,
                    get_next_use_case, prepare_first_question_data)

use_case_bp = Blueprint("use_case", __name__)


@use_case_bp.route("/api/practice/submit", methods=["POST"])
@login_required
def submit_answer():
    """
    Process answers submitted by the user for a use case, evaluate correctness, and respond appropriately.
    """
    app.logger.debug("Received submit request")
    app.logger.debug("Request method: %s", request.method)
    app.logger.debug("Request data: %s", request.json)

    data = request.get_json()
    app.logger.info(f"Received data: {data}")

    use_case_id = data.get("useCaseId")
    lesson_id = data.get("lessonId")
    answers_data = data.get("answers")

    app.logger.debug(f"use_case_id: {use_case_id}")
    app.logger.debug(f"answers: {answers_data}")
    app.logger.debug(f"lesson: {lesson_id}")

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
            lesson_id=lesson_id,
        )
        db.session.add(attempt)
        results.append({"questionId": question_id, "isCorrect": is_correct})

        if not is_correct:
            has_mistake = True

    db.session.commit()

    if has_mistake:
        # Find a similar use case based on risk factors
        similar_use_case = find_similar_use_case(
            use_case_id, current_user.id, current_user.lesson_id
        )
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
