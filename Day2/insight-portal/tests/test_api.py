"""FastAPI 테스트"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    """헬스 체크 테스트"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()['ok'] is True

def test_register_success():
    """회원가입 성공 테스트"""
    response = client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 201
    data = response.json()
    assert data['ok'] is True
    assert data['user']['email'] == "test@example.com"

def test_register_weak_password():
    """약한 비밀번호 테스트"""
    response = client.post("/auth/register", json={
        "email": "test2@example.com",
        "password": "123"
    })
    assert response.status_code == 400
    data = response.json()
    assert 'WEAK_PASSWORD' in str(data)

def test_register_duplicate_email():
    """중복 이메일 테스트"""
    # 첫 번째 등록
    client.post("/auth/register", json={
        "email": "duplicate@example.com",
        "password": "password123"
    })
    
    # 중복 등록 시도
    response = client.post("/auth/register", json={
        "email": "duplicate@example.com",
        "password": "password456"
    })
    assert response.status_code == 409
    data = response.json()
    assert 'DUPLICATE_EMAIL' in str(data)

def test_get_kpis():
    """KPI 조회 테스트"""
    response = client.get("/api/kpis")
    assert response.status_code == 200
    data = response.json()
    assert data['ok'] is True
    assert 'data' in data
    assert 'total_revenue' in data['data']

def test_get_charts():
    """차트 목록 조회 테스트"""
    response = client.get("/api/charts")
    assert response.status_code == 200
    data = response.json()
    assert data['ok'] is True
    assert 'charts' in data
