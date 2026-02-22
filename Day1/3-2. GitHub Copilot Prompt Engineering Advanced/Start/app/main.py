from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Review API")


@app.get("/health")
async def health():
    """헬스 체크"""
    return {"ok": True, "status": "healthy"}


# TODO: reviews 라우터를 포함해야 함
# from app.routes import reviews
# app.include_router(reviews.router, prefix="/api")
