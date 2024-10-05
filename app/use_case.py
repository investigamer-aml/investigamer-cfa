""" Module to handle endpoints for use case related stuff
"""

from flask import Blueprint, jsonify, request, current_app as app
from flask_login import current_user, login_required
from app import db
from dbb.models import Options, Questions, UserAnswers, UseCases

from .utils import (find_similar_use_case, get_first_question_of_use_case,
                    get_lessons_use_case_count, get_next_use_case,
                    get_users_correct_use_cases_per_lesson,
                    prepare_first_question_data)

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

    if not use_case_id or not answers_data or not lesson_id:
        return (
            jsonify({"error": "Missing use case ID, lesson ID, or answers data"}),
            400,
        )

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

    next_use_case = None
    is_similar_use_case = False

    if has_mistake:
        similar_use_case = find_similar_use_case(
            use_case_id, current_user.id, lesson_id
        )
        if similar_use_case:
            next_use_case = similar_use_case
            is_similar_use_case = True

    if not next_use_case:
        # If no mistake or no similar use case found, get the next sequential use case
        next_use_case = get_next_use_case(use_case_id, current_user.id, lesson_id)

    completed_use_cases = get_users_correct_use_cases_per_lesson(
        lesson_id, current_user.id
    )
    total_use_cases = get_lessons_use_case_count(lesson_id)

    response_data = {
        "message": "Answer submitted successfully",
        "results": results,
        "completedUseCases": completed_use_cases,
        "totalUseCases": total_use_cases,
        "isComplete": next_use_case is None,
    }

    if next_use_case:
        app.logger.info(f"Next use case: {next_use_case.id}")
        app.logger.debug(f"Next use case questions: {next_use_case.questions}")
        first_question = get_first_question_of_use_case(next_use_case.id)
        response_data["nextUseCase"] = {
            "useCaseId": next_use_case.id,
            "description": next_use_case.description,
            "firstQuestion": prepare_first_question_data(first_question),
            "lessonId": next_use_case.lesson_id,
        }
        response_data["isSimilarUseCase"] = is_similar_use_case
    else:
        app.logger.info("No next use case available")

    return jsonify(response_data), 200


@use_case_bp.route("/api/practice_v2/submit", methods=["POST"])
@login_required
def submit_answer_v2():
    """
    Process answers submitted by the user for a use case in practice v2,
    evaluate correctness based on risk analyst decision, and respond appropriately.
    """
    app.logger.debug("Received submit request for practice v2")
    app.logger.debug("Request method: %s", request.method)
    app.logger.debug("Request data: %s", request.json)

    data = request.get_json()
    app.logger.info(f"Received data: {data}")

    use_case_id = data.get("useCaseId")
    lesson_id = data.get("lessonId")
    answer = data.get("answer")

    app.logger.debug(f"use_case_id: {use_case_id}")
    app.logger.debug(f"answer: {answer}")
    app.logger.debug(f"lesson: {lesson_id}")

    if not use_case_id or not answer or not lesson_id:
        return jsonify({"error": "Missing use case ID, lesson ID, or answer data"}), 400

    use_case = UseCases.query.get(use_case_id)
    if not use_case:
        return jsonify({"error": "Use case not found"}), 404

    # For simplicity, we'll consider 'escalate' as the correct answer
    # In a real scenario, you'd have a more sophisticated way to determine correctness
    is_correct = (answer == 'escalate')

    user_answer = UserAnswers(
        user_id=current_user.id,
        use_case_id=int(use_case_id),
        lesson_id=int(lesson_id),
        is_correct=is_correct,
    )
    db.session.add(user_answer)
    db.session.commit()

    response_data = {
        "message": "Answer submitted successfully",
        "result": {"isCorrect": is_correct},
    }

    return jsonify(response_data), 200
