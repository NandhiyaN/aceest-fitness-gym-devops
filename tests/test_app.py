import os
import tempfile
import pytest

from app import app, initialize_database


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()

    app.config["TESTING"] = True
    app.config["DATABASE"] = db_path
    app.config["WTF_CSRF_ENABLED"] = False

    with app.test_client() as client:
        with app.app_context():
            initialize_database()
        yield client

    os.close(db_fd)
    os.unlink(db_path)


def login(client):
    return client.post(
        "/login",
        data={
            "username": "admin@aceest.com",
            "password": "Admin@123"
        },
        follow_redirects=True
    )


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "UP"


def test_login_success(client):
    response = login(client)
    assert response.status_code == 200
    assert b"Dashboard" in response.data


def test_add_client(client):
    login(client)

    response = client.post(
        "/clients/add",
        data={
            "name": "Rahul",
            "age": "30",
            "height": "175",
            "weight": "72",
            "membership_status": "Active",
            "membership_end": "2026-12-31"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Rahul" in response.data


def test_generate_program(client):
    login(client)

    client.post(
        "/clients/add",
        data={
            "name": "Meera",
            "membership_status": "Active"
        },
        follow_redirects=True
    )

    response = client.get("/clients/Meera/generate-program", follow_redirects=True)

    assert response.status_code == 200
    assert b"Program generated for Meera" in response.data


def test_add_workout(client):
    login(client)

    client.post(
        "/clients/add",
        data={
            "name": "Arjun",
            "membership_status": "Active"
        },
        follow_redirects=True
    )

    response = client.post(
        "/workouts/add",
        data={
            "client_name": "Arjun",
            "workout_date": "2026-04-01",
            "workout_type": "Strength",
            "duration": "45",
            "notes": "Upper body strength session"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Upper body strength session" in response.data