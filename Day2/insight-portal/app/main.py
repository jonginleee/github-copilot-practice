"""FastAPI 메인 앱"""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routes import auth, metrics

app = FastAPI(title="Insight Portal", version="1.0.0")

# 라우터 등록
app.include_router(auth.router)
app.include_router(metrics.router)

@app.get("/health")
def health():
    """헬스 체크"""
    return {"ok": True, "status": "up"}

@app.get("/", response_class=HTMLResponse)
def index():
    """간단 대시보드 화면"""
    html = """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Insight Portal</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; }
            h1 { color: #333; }
            .api-link { display: inline-block; margin: 10px; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 4px; }
            .api-link:hover { background: #0056b3; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Insight Portal</h1>
            <p>데이터 분석 결과를 API로 제공합니다.</p>
            
            <h2>API 엔드포인트</h2>
            <a class="api-link" href="/api/kpis" target="_blank">GET /api/kpis</a>
            <a class="api-link" href="/api/charts" target="_blank">GET /api/charts</a>
            <a class="api-link" href="/docs" target="_blank">API 문서</a>
        </div>
    </body>
    </html>
    """
    return html
