import pytest

import dbb as db
import main
from dbb.models import Lessons, UserLessonInteraction, Users


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


@pytest.fixture
def init_database():
    user1 = Users(id=1, username="testuser", email="test@example.com")
    lesson1 = Lessons(id=1, title="Intro to Testing")
    db.session.add(user1)
    db.session.add(lesson1)
    db.session.commit()

    yield  # this is where the testing happens

    db.session.remove()
    db.drop_all()


def test_register_user(client):
    """Test user registration."""
    response = client.post(
        "/register",
        data={
            "username": "testuser",
            "email": "test@example.com",
            "password": "securepassword",
        },
    )
    assert response.status_code == 201
    assert b"User registered successfully" in response.data


def test_lesson_completion(client, init_database):
    # Simulate a user completing a lesson
    app.update_lesson_progress(user_id=1, lesson_id=1, progress=100)
    interaction = UserLessonInteraction.query.first()
    assert interaction.completed is True
    assert interaction.lesson_id == 1


def test_get_next_lesson(client, init_database):
    # Assuming the user has completed the first lesson
    app.update_lesson_progress(user_id=1, lesson_id=1, progress=100)
    next_lesson = app.get_next_lesson(user_id=1)
    assert next_lesson is None  # Adjust based on your actual next lesson logic


def test_progress_update(client, init_database):
    app.update_lesson_progress(user_id=1, lesson_id=1, progress=50)
    interaction = UserLessonInteraction.query.first()
    assert interaction.progress == 50
    assert interaction.completed is False
