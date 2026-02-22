# Insight Portal - 데이터 분석 → API 서비스화 프로젝트

## 프로젝트 목표

주문 데이터(`orders.csv`)를 분석해 KPI와 차트를 생성하고, FastAPI로 서비스화하는 하루 프로젝트

## 환경 셋업

```bash
# 가상환경 생성 및 활성화
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
# source .venv/bin/activate  # macOS/Linux

# 의존성 설치
pip install -r requirements.txt

# 데이터 생성
python tools/generate_data.py

# 테스트 실행
pytest -q

# API 서버 실행
uvicorn app.main:app --reload
```

## 구조

```
insight-portal/
  data/orders.csv           # 주문 데이터
  analysis/
    kpi.py                  # KPI 계산 로직
    viz.py                  # 차트 생성
  app/
    main.py                 # FastAPI 앱
    routes/
      auth.py               # 회원가입 API
      metrics.py            # KPI/차트 API
    security.py             # 비밀번호 해싱
    storage.py              # 인메모리 저장소
  tests/                    # pytest 테스트
  reports/                  # 분석 리포트 & 차트
```

## API 엔드포인트

- `GET /api/kpis` - KPI 데이터 조회
- `GET /api/charts` - 차트 목록 조회
- `POST /auth/register` - 회원가입
- `GET /` - 간단 대시보드 화면

## 검증 기준

✅ `pytest -q` 전체 통과  
✅ `GET /api/kpis` 정상 응답(200)  
✅ `POST /auth/register` 상태 코드(201/400/409) 정확  
✅ `reports/report.md` 분석 리포트 작성됨
