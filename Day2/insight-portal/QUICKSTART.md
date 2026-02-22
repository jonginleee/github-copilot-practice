# 빠른 시작 가이드

## 1. 환경 설정

```powershell
cd "Day2/insight-portal"
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 2. 데이터 생성

```powershell
python tools/generate_data.py
```

## 3. 테스트 실행

```powershell
pytest -v
```

## 4. API 서버 실행

```powershell
uvicorn app.main:app --reload
```

브라우저에서 접속:
- http://127.0.0.1:8000 (대시보드)
- http://127.0.0.1:8000/docs (API 문서)

## 5. 차트 생성 테스트

```python
from analysis.kpi import load_orders
from analysis.viz import generate_charts

df = load_orders('data/orders.csv')
generate_charts(df)
```

`reports/charts/` 폴더에서 차트 확인

## 문제 해결

### ModuleNotFoundError
```powershell
# PYTHONPATH 설정 (프로젝트 루트에서 실행)
$env:PYTHONPATH = "."
```

### 한글 폰트 문제 (matplotlib)
Windows에서는 'Malgun Gothic', Mac에서는 'AppleGothic' 사용

### 테스트 실패 (첫 실행 시)
먼저 `python tools/generate_data.py`로 데이터 생성 필요
