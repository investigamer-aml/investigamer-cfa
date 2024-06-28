import pytest
from flask import session
from flask_login import current_user, login_user

from app import create_app, db
from dbb.models import (DifficultyLevel, Lessons, Options, Questions, UseCases,
                        Users)


@pytest.fixture(scope="module")
def app():
    """
    Fixture to create a Flask application instance for testing.

    This fixture sets up the Flask application with the "TestingConfig" configuration,
    enables testing mode, and disables CSRF protection for testing purposes.

    Returns:
        Flask: The Flask application instance configured for testing.
    """
    app = create_app("TestingConfig")
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False
    return app


@pytest.fixture(scope="module")
def client(app):
    """
    Fixture to create a Flask test client instance for testing.

    This fixture creates a test client instance for the Flask application instance
    returned by the "app" fixture.

    Returns:
        Flask: The Flask test client instance configured for testing.
    """
    return app.test_client()


@pytest.fixture(scope="module")
def init_database(app):
    """
    Fixture to initialize the database for testing.

    This fixture creates all tables in the database and adds a test difficulty level and lesson.
    """
    with app.app_context():
        db.create_all()
        difficulty = DifficultyLevel(level="Medium")
        db.session.add(difficulty)
        lesson = Lessons(title="Test Lesson")
        db.session.add(lesson)
        db.session.commit()
        yield db
        db.drop_all()


@pytest.fixture(scope="function")
def logged_in_user(app, client, init_database):
    """
    Fixture to create a logged-in user for testing.

    This fixture creates a user in the database and logs them in using the test client.
    """
    with app.app_context():
        user = Users(
            email="test@example.com",
            first_name="Test",
            last_name="User",
            lesson_id=1,
            score=0,
            use_case_difficulty="Medium",
        )
        user.set_password("password")
        init_database.session.add(user)
        init_database.session.commit()

        client.post(
            "/api/login",
            json={"login_input": "test@example.com", "password": "password"},
        )

        yield user

        init_database.session.delete(user)
        init_database.session.commit()


def test_login(app, client, init_database):
    """
    Test the login functionality.

    This test creates a user in the database and attempts to log them in using the test client.
    """
    with app.app_context():
        user = Users(
            email="login_test@example.com",
            first_name="Login",
            last_name="Test",
            lesson_id=1,
            score=0,
            use_case_difficulty="Medium",
        )
        user.set_password("password")
        init_database.session.add(user)
        init_database.session.commit()

        response = client.post(
            "/api/login",
            json={"login_input": "login_test@example.com", "password": "password"},
        )
        assert response.status_code == 200
        assert b"Login successful" in response.data


def test_get_practice_data(app, client, init_database, logged_in_user):
    """
    Test the get practice data functionality.

    This test creates a use case in the database and retrieves the practice data for the lesson.
    """
    with app.app_context():
        difficulty = DifficultyLevel.query.filter_by(level="Medium").first()
        lesson = Lessons.query.first()
        use_case = UseCases(
            description="Test use case",
            type="KYC",
            lesson_id=lesson.id,
            created_by_user=logged_in_user.id,
            difficulty_id=difficulty.id,
        )
        init_database.session.add(use_case)
        init_database.session.commit()

        question = Questions(use_case_id=use_case.id, text="Test question")
        init_database.session.add(question)
        init_database.session.commit()

        response = client.get(f"/api/practice/{lesson.id}")
        assert response.status_code == 200
        assert b"Test use case" in response.data


def test_submit_answer(app, client, init_database, logged_in_user):
    """
    Test the submit answer functionality.

    This test creates a use case, question, and option in the database and submits an answer for the use case.
    """
    with app.app_context():
        difficulty = DifficultyLevel.query.filter_by(level="Medium").first()
        lesson = Lessons.query.first()
        use_case = UseCases(
            description="Test use case",
            type="KYC",
            lesson_id=lesson.id,
            created_by_user=logged_in_user.id,
            difficulty_id=difficulty.id,
        )
        init_database.session.add(use_case)
        init_database.session.commit()

        question = Questions(use_case_id=use_case.id, text="Test question")
        init_database.session.add(question)
        init_database.session.commit()

        option = Options(question_id=question.id, text="Test option", is_correct=True)
        init_database.session.add(option)
        init_database.session.commit()

        response = client.post(
            "/api/practice/submit",
            json={
                "useCaseId": use_case.id,
                "lessonId": lesson.id,
                "answers": [{"questionId": question.id, "answer": option.id}],
            },
        )
        assert response.status_code == 200
        assert b"Answer submitted successfully" in response.data
