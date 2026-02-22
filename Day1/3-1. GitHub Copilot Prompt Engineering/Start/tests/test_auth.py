from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_success():
    r = client.post("/auth/register", json={"email": "user@example.com", "password": "Abcd!234"})
    assert r.status_code == 201
    data = r.json()
    assert data["ok"] is True
    assert data["user"]["email"] == "user@example.com"
    assert "password" not in data["user"]
    assert "password_hash" not in data["user"]

def test_register_rejects_weak_password():
    r = client.post("/auth/register", json={"email": "user2@example.com", "password": "weakpass"})
    assert r.status_code == 400
    data = r.json()
    assert data["ok"] is False
    assert data["error"]["code"] == "WEAK_PASSWORD"

def test_register_rejects_bad_email():
    r = client.post("/auth/register", json={"email": "not-an-email", "password": "Abcd!234"})
    assert r.status_code == 400
    data = r.json()
    assert data["ok"] is False
    assert data["error"]["code"] == "INVALID_EMAIL"

def test_register_rejects_duplicate_email():
    client.post("/auth/register", json={"email": "dup@example.com", "password": "Abcd!234"})
    r = client.post("/auth/register", json={"email": "dup@example.com", "password": "Abcd!234"})
    assert r.status_code == 409
    data = r.json()
    assert data["ok"] is False
    assert data["error"]["code"] == "DUPLICATE_EMAIL"
