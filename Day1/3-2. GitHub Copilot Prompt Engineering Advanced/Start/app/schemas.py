from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ReviewCreateRequest(BaseModel):
    """리뷰 작성 요청"""
    product_id: str = Field(..., min_length=1, max_length=50)
    rating: int = Field(..., ge=1, le=5)
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1, max_length=2000)
    reviewer: str = Field(..., min_length=1, max_length=50)


class ReviewUpdateRequest(BaseModel):
    """리뷰 수정 요청"""
    rating: Optional[int] = Field(None, ge=1, le=5)
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    content: Optional[str] = Field(None, min_length=1, max_length=2000)


class ReviewResponse(BaseModel):
    """리뷰 응답"""
    id: int
    product_id: str
    rating: int
    title: str
    content: str
    reviewer: str
    created_at: str
    updated_at: str


class ErrorResponse(BaseModel):
    """에러 응답"""
    ok: bool = False
    error_code: str
    message: str


class SuccessResponse(BaseModel):
    """성공 응답 (단일 리뷰)"""
    ok: bool = True
    review: ReviewResponse


class RatingStats(BaseModel):
    """평점 통계"""
    total: int
    average_rating: float
    rating_distribution: dict  # {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4}


class ReviewListResponse(BaseModel):
    """리뷰 목록 응답"""
    ok: bool = True
    product_id: str
    reviews: list[ReviewResponse]
    stats: RatingStats
