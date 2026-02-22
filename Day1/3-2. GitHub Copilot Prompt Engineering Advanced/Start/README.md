# 상품 리뷰 API 요구사항

## 환경 셋업

```bash
cd "Day1/3-2. GitHub Copilot Prompt Engineering Advanced/Start"
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
pip install fastapi uvicorn[standard] pytest pydantic
pytest -q  # 테스트 실행
```

## 데이터 모델 (Review)

```json
{
  "id": 1,
  "product_id": "PROD-001",
  "rating": 4,
  "title": "좋은 상품",
  "content": "품질이 우수합니다",
  "reviewer": "홍길동",
  "created_at": "2025-01-15T10:30:00",
  "updated_at": "2025-01-15T10:30:00"
}
```

#### 엔드포인트

| 메서드 | 경로 | 설명 |
|-------|------|------|
| POST | `/reviews` | 리뷰 작성 |
| GET | `/reviews/{review_id}` | 리뷰 조회 |
| GET | `/reviews/products/{product_id}` | 상품별 리뷰 목록 |
| PUT | `/reviews/{review_id}` | 리뷰 수정 |
| DELETE | `/reviews/{review_id}` | 리뷰 삭제 |

#### GET /reviews/products/{product_id} - 상품별 리뷰 목록

**쿼리 파라미터**:
- `sort`: `rating_desc` (높은 평점순), `rating_asc` (낮은 평점순), `recent` (최신순)
- `min_rating`: 최소 평점 (1-5)

**응답 예시**:

```json
{
  "ok": true,
  "product_id": "PROD-001",
  "reviews": [
    {
      "id": 1,
      "rating": 5,
      "title": "정말 좋아요",
      "content": "배송도 빠르고 품질도 제일 좋습니다",
      "reviewer": "김철수",
      "created_at": "2025-01-15T10:30:00"
    }
  ],
  "stats": {
    "total": 10,
    "average_rating": 4.2,
    "rating_distribution": {
      "5": 6,
      "4": 2,
      "3": 1,
      "2": 1,
      "1": 0
    }
  }
}
```

#### POST /reviews - 리뷰 작성

**입력 (ReviewCreateRequest)**:

```json
{
  "product_id": "PROD-001",
  "rating": 4,
  "title": "좋은 상품",
  "content": "품질이 합리적입니다",
  "reviewer": "이순신"
}
```

**응답 (성공 201)**:

```json
{
  "ok": true,
  "review": {
    "id": 1,
    "product_id": "PROD-001",
    "rating": 4,
    "title": "좋은 상품",
    "content": "품질이 합리적입니다",
    "reviewer": "이순신",
    "created_at": "2025-01-15T10:30:00",
    "updated_at": "2025-01-15T10:30:00"
  }
}
```

**에러 응답 (400 Bad Request)**:

```json
{
  "ok": false,
  "error_code": "INVALID_RATING",
  "message": "평점은 1~5 사이의 정수여야 합니다"
}
```

#### DELETE /reviews/{review_id}

**응답 (성공 204)**:
- 본문 없음

## 검증 규칙

### POST /reviews
- `rating`: 1~5 정수 (벗어나면 400 INVALID_RATING)
- `title`: 1~100자 (벗어나면 400 INVALID_TITLE)
- `content`: 1~2000자 (벗어나면 400 INVALID_CONTENT)
- `reviewer`: 1~50자 (벗어나면 400 INVALID_REVIEWER)

### PUT /reviews/{review_id}
- `review_id` 없으면 404 REVIEW_NOT_FOUND
- rating/title/content 중 1개 이상 제공되어야 함 (없으면 400 NO_FIELDS_TO_UPDATE)
- 검증은 POST와 동일

### DELETE /reviews/{review_id}
- `review_id` 없으면 404 REVIEW_NOT_FOUND

## 성공 기준

✅ `pytest -q` 6개 테스트 모두 PASSED  
✅ 평점 집계, 필터링, 정렬 정상 작동  
✅ 모든 응답이 스펙 준수 (ok, error_code, message 필수)
