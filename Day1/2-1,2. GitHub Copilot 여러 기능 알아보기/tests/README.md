# 테스트 폴더

이 폴더에는 실습 9(자동화된 테스트 생성)에서 생성될 테스트 파일들이 위치합니다.

## 생성될 파일 예시

- `test_bank_account.py`: BankAccount 클래스 테스트
- `test_invoice.py`: invoice 모듈 테스트

## 테스트 실행 방법

```powershell
# 모든 테스트 실행
pytest

# 특정 파일만 실행
pytest tests/test_invoice.py

# 상세 출력
pytest -v

# 빠른 실행 (요약만)
pytest -q
```

## pytest 설치

```powershell
pip install pytest
```
