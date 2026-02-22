# 데이터 디렉토리

## orders.csv

`tools/generate_data.py`로 생성되는 샘플 주문 데이터

### 컬럼 정보

| 컬럼 | 타입 | 설명 | 예시 |
|------|------|------|------|
| order_id | string | 주문 ID | ORD-00001 |
| order_date | datetime | 주문 날짜 | 2025-01-15 |
| region | string | 지역 | 서울, 경기, 부산, 대구, 기타 |
| channel | string | 채널 | 온라인, 모바일, 오프라인 |
| revenue | int | 매출 (원) | 100000 |
| cost | int | 비용 (원) | 60000 |
| is_returned | bool | 반품 여부 | True/False |

### 데이터 생성

```bash
python tools/generate_data.py
```

기본 1000개 행, 최근 6개월 데이터 생성
