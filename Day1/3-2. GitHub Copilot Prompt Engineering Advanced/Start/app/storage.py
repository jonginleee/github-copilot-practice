"""인메모리 데이터 저장소"""

from datetime import datetime
from typing import Optional, Dict, List

# 다음 리뷰 ID 자동증가
next_review_id = 1

# 리뷰 저장소: {review_id: review_dict}
reviews_db: Dict[int, dict] = {}


def get_next_review_id() -> int:
    """다음 리뷰 ID 반환"""
    global next_review_id
    current_id = next_review_id
    next_review_id += 1
    return current_id


def save_review(product_id: str, rating: int, title: str, content: str, reviewer: str) -> dict:
    """리뷰 저장"""
    review_id = get_next_review_id()
    now = datetime.now().isoformat()
    
    review = {
        "id": review_id,
        "product_id": product_id,
        "rating": rating,
        "title": title,
        "content": content,
        "reviewer": reviewer,
        "created_at": now,
        "updated_at": now,
    }
    
    reviews_db[review_id] = review
    return review


def get_review(review_id: int) -> Optional[dict]:
    """리뷰 조회"""
    return reviews_db.get(review_id)


def get_reviews_by_product(
    product_id: str,
    sort: str = "rating_desc",
    min_rating: Optional[int] = None,
) -> tuple[List[dict], dict]:
    """
    상품별 리뷰 조회 및 통계 계산
    
    Returns:
        (리뷰 목록, 통계 dict)
    """
    # 해당 상품의 리뷰 필터링
    product_reviews = [
        r for r in reviews_db.values()
        if r["product_id"] == product_id
    ]
    
    # 최소 평점 필터
    if min_rating:
        product_reviews = [r for r in product_reviews if r["rating"] >= min_rating]
    
    # 정렬
    if sort == "rating_desc":
        product_reviews.sort(key=lambda r: r["rating"], reverse=True)
    elif sort == "rating_asc":
        product_reviews.sort(key=lambda r: r["rating"])
    elif sort == "recent":
        product_reviews.sort(key=lambda r: r["created_at"], reverse=True)
    
    # 통계 계산
    if product_reviews:
        avg_rating = sum(r["rating"] for r in product_reviews) / len(product_reviews)
        avg_rating = round(avg_rating, 1)
    else:
        avg_rating = 0.0
    
    # 평점 분포
    rating_dist = {str(i): 0 for i in range(1, 6)}
    for review in product_reviews:
        rating_dist[str(review["rating"])] += 1
    
    stats = {
        "total": len(product_reviews),
        "average_rating": avg_rating,
        "rating_distribution": rating_dist,
    }
    
    return product_reviews, stats


def update_review(review_id: int, **kwargs) -> Optional[dict]:
    """리뷰 수정"""
    review = reviews_db.get(review_id)
    if not review:
        return None
    
    # 수정 가능한 필드
    updatable_fields = ["rating", "title", "content"]
    for field in updatable_fields:
        if field in kwargs:
            review[field] = kwargs[field]
    
    review["updated_at"] = datetime.now().isoformat()
    return review


def delete_review(review_id: int) -> bool:
    """리뷰 삭제"""
    if review_id in reviews_db:
        del reviews_db[review_id]
        return True
    return False


def clear_all():
    """모든 리뷰 삭제 (테스트용)"""
    global reviews_db, next_review_id
    reviews_db.clear()
    next_review_id = 1
